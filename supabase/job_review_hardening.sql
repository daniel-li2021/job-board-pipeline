-- PROPOSAL ONLY. Requires approval, an Auth sign-in UI, and an enrolled editor.
-- Never run as part of deploy/crawler/Pages. Keep public reads; restrict writes.
begin;
create schema if not exists private;
revoke all on schema private from public;
grant usage on schema private to authenticated;
create table if not exists private.job_review_allowlist (
  user_id uuid primary key references auth.users(id) on delete cascade
);
revoke all on private.job_review_allowlist from public, anon, authenticated;
-- Enroll the approved owner's auth.users UUID here before executing this proposal.
do $$ begin
  if not exists (select 1 from private.job_review_allowlist) then
    raise exception 'Enroll an approved editor and configure sign-in before applying';
  end if;
end $$;
create or replace function private.is_job_review_editor()
returns boolean language sql stable security definer set search_path = ''
as $$ select exists (select 1 from private.job_review_allowlist where user_id = auth.uid()) $$;
revoke all on function private.is_job_review_editor() from public, anon;
grant execute on function private.is_job_review_editor() to authenticated;
alter table public.job_review_status enable row level security;
revoke insert, update, delete on public.job_review_status from public, anon, authenticated;
-- Existing column grants also need removal, otherwise table-level REVOKE is insufficient.
revoke insert (canonical_job_key, status, deleted, updated_at),
  update (canonical_job_key, status, deleted, updated_at)
  on public.job_review_status from public, anon, authenticated;
grant select on public.job_review_status to anon, authenticated;
grant insert (canonical_job_key, status, deleted, updated_at),
  update (canonical_job_key, status, deleted, updated_at)
  on public.job_review_status to authenticated;
drop policy if exists "Public can insert job review status" on public.job_review_status;
drop policy if exists "Public can update job review status" on public.job_review_status;
drop policy if exists "Allowlisted users can insert job review status" on public.job_review_status;
drop policy if exists "Allowlisted users can update job review status" on public.job_review_status;
create policy "Allowlisted users can insert job review status"
on public.job_review_status for insert to authenticated
with check (private.is_job_review_editor());
create policy "Allowlisted users can update job review status"
on public.job_review_status for update to authenticated
using (private.is_job_review_editor()) with check (private.is_job_review_editor());
-- Restrictive guards also constrain any other permissive authenticated write policies.
drop policy if exists "Require approved editor for every insert" on public.job_review_status;
drop policy if exists "Require approved editor for every update" on public.job_review_status;
create policy "Require approved editor for every insert"
on public.job_review_status as restrictive for insert to authenticated
with check (private.is_job_review_editor());
create policy "Require approved editor for every update"
on public.job_review_status as restrictive for update to authenticated
using (private.is_job_review_editor()) with check (private.is_job_review_editor());
commit;
