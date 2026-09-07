# Pacific scheduler

Status: deployed and verified in `us-west-1` on 2026-09-07. GitHub cron blocks and
the redundant scheduled Pages fallback are removed.

| Workflow | America/Los_Angeles targets | AWS expression |
|---|---|---|
| board-jobs.yml | 08:00, 17:00 | `cron(0 8,17 * * ? *)` |
| daily-jobs.yml | 08:10, 17:10 | `cron(10 8,17 * * ? *)` |
| official-careers.yml | 08:20, 17:20 | `cron(20 8,17 * * ? *)` |

All three schedules use `America/Los_Angeles`, automatically follow DST, and set the
flexible window to OFF. Scheduler has minute-level precision; GitHub runner
queuing can still delay actual execution. Discovery workflows remain independent,
manual dispatch stays available, and successful `workflow_run` events continue to
reconcile and publish Pages using latest main.

One Lambda, secret reference, execution roles, schedule group, and encrypted SQS
failure queue serve all three schedules. Scheduler retries delivery up to three
times within 15 minutes. Lambda retries execution twice within 15 minutes and
routes exhausted errors to the same queue. Logs retain receipts for 14 days;
failed messages retain for 14 days. Check the queue and Lambda Errors metric if
runs stop arriving. The function fetches the token each invocation so rotating the
secret needs no redeployment. Delivery is at-least-once: a lost HTTP response can
cause duplicate dispatch. Existing workflow concurrency prevents simultaneous
runs of each pipeline, but is not an exactly-once guarantee.

## Deployment and cutover

1. Authenticate AWS and GitHub. Inspect existing Scheduler groups, schedules and
   Lambda functions in the target account/region before deploying; reuse an
   existing compatible dispatcher if one exists.
2. Use an existing Secrets Manager secret containing a **plain-text GitHub token**
   restricted to this repository with Actions write permission. Use the default
   Secrets Manager encryption key; a customer KMS key additionally requires
   `kms:Decrypt` on that key in DispatchRole. Never put the token in source,
   shell arguments, logs, or CloudFormation parameters. A local `gh` login token
   is not automatically suitable as the durable scheduler credential.
3. Publish workflow probe inputs and validate the template with `cfn-lint` and
   `aws cloudformation validate-template`. Deploy in the chosen region:

   ```sh
   aws cloudformation deploy --stack-name job-board-scheduler \
     --template-file infra/scheduler/template.yaml --capabilities CAPABILITY_IAM \
     --parameter-overrides GitHubTokenSecretArn="$SCHEDULER_SECRET_ARN" ScheduleState=ENABLED
   ```

4. Read stack outputs for group, role and Lambda ARNs. For each of the three
   discovery workflows, create one **temporary one-time Scheduler schedule** in
   that same group, 2–3 minutes ahead, with flexible window OFF, the same role,
   Lambda target, retry/DLQ settings and a unique input such as:

   ```json
   {"workflow":"board-jobs.yml","probe_id":"board-YYYYMMDDTHHMMSSZ"}
   ```

   Use `--action-after-completion DELETE`. The `scheduler_probe` workflow input
   records receipt while skipping crawling, scoring, output commits and alerts.
   This exercises Scheduler → Lambda → authenticated GitHub dispatch → runner.
   Match the CloudWatch 204 receipt to the GitHub run named
   `Scheduler probe <probe_id>`; require `event=workflow_dispatch`, branch main,
   and successful completion. A direct Lambda invocation alone does not verify
   the Scheduler role or delivery path. Wait at most 10 minutes for each probe;
   inspect logs and the failure queue on failure, without unbounded retries.
5. Verify successful Pages publication triggered by each completed discovery workflow.
6. Read back all three AWS schedule expressions, timezones, states and flexible
   windows, and confirm main has no GitHub cron.
7. On cutover failure, restore GitHub cron and leave AWS recurring schedules
   disabled. For rollback after cutover, disable AWS first, then restore cron.

Offline dispatcher regression check:

```sh
python3 infra/scheduler/test_scheduler.py
```

References: [Scheduler timing and DST](https://docs.aws.amazon.com/scheduler/latest/UserGuide/schedule-types.html),
[asynchronous Lambda delivery](https://docs.aws.amazon.com/lambda/latest/dg/with-eventbridge-scheduler.html),
[GitHub workflow dispatch](https://docs.github.com/en/rest/actions/workflows#create-a-workflow-dispatch-event).
