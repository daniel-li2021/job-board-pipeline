-- Run once in the Supabase SQL editor, then add each permitted email below.
create schema if not exists private;

create table if not exists private.job_review_allowlist (
  email text primary key check (email = lower(email))
);

revoke all on schema private from public;
revoke all on table private.job_review_allowlist from public, anon, authenticated;
grant usage on schema private to authenticated;

create or replace function private.is_job_review_editor()
returns boolean
language sql
stable
security definer
set search_path = ''
as $$
  select (select auth.uid()) is not null
    and coalesce((select auth.jwt() ->> 'is_anonymous'), 'false') <> 'true'
    and exists (
      select 1
      from private.job_review_allowlist
      where email = lower(coalesce((select auth.jwt() ->> 'email'), ''))
    );
$$;

revoke all on function private.is_job_review_editor() from public;
grant execute on function private.is_job_review_editor() to authenticated;

create table if not exists public.job_review_status (
  canonical_job_key text primary key check (length(canonical_job_key) between 1 and 2048),
  status text not null default 'unreviewed'
    check (status in ('unreviewed', 'in_progress', 'applied_complete')),
  deleted boolean not null default false,
  updated_at timestamptz not null default now()
);

alter table public.job_review_status enable row level security;
revoke all on table public.job_review_status from anon, authenticated;
grant select on table public.job_review_status to anon, authenticated;
grant insert (canonical_job_key, status, deleted, updated_at),
  update (status, deleted, updated_at)
  on table public.job_review_status to authenticated;

drop policy if exists "Public can read job review status" on public.job_review_status;
create policy "Public can read job review status"
on public.job_review_status for select
to anon, authenticated
using (true);

drop policy if exists "Allowlisted users can insert job review status" on public.job_review_status;
create policy "Allowlisted users can insert job review status"
on public.job_review_status for insert
to authenticated
with check ((select private.is_job_review_editor()));

drop policy if exists "Allowlisted users can update job review status" on public.job_review_status;
create policy "Allowlisted users can update job review status"
on public.job_review_status for update
to authenticated
using ((select private.is_job_review_editor()))
with check ((select private.is_job_review_editor()));

-- Replace these examples with the real lowercase emails allowed to edit.
-- insert into private.job_review_allowlist (email)
-- values ('you@example.com'), ('teammate@example.com')
-- on conflict (email) do nothing;
