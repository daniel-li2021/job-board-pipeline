-- Run once in the Supabase SQL editor. Anyone using the public dashboard can edit.
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
  update (canonical_job_key, status, deleted, updated_at)
  on table public.job_review_status to anon, authenticated;

drop policy if exists "Public can read job review status" on public.job_review_status;
create policy "Public can read job review status"
on public.job_review_status for select
to anon, authenticated
using (true);

drop policy if exists "Allowlisted users can insert job review status" on public.job_review_status;
drop policy if exists "Allowlisted users can update job review status" on public.job_review_status;
drop policy if exists "Public can insert job review status" on public.job_review_status;
drop policy if exists "Public can update job review status" on public.job_review_status;

create policy "Public can insert job review status"
on public.job_review_status for insert
to anon, authenticated
with check (true);

create policy "Public can update job review status"
on public.job_review_status for update
to anon, authenticated
using (true)
with check (true);

-- Remove the previous allowlist objects if that version of this setup ran.
create schema if not exists private;
drop function if exists private.is_job_review_editor();
drop table if exists private.job_review_allowlist;
