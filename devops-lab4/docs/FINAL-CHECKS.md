# Lab 4 Final Checks

[Project overview](../README.md) · [Detailed report](../REPORT.md) · [Screenshot gallery](EVIDENCE.md)

The documentation includes the supplied evidence. The following checks distinguish a working component from proof of each requested behaviour.

## Question 1 Pipeline gate

The pass-fail-pass sequence is captured. The Deployment Gate is an approval message, so describe it as a gate rather than a deployed application. The route tests use Flask's in-process test client. [S05](EVIDENCE.md#s05), [S08](EVIDENCE.md#s08), [S11](EVIDENCE.md#s11)

## Question 2 Blue-Green switching

The attempted switch in S14 still returns `v1`. S15 only shows requests 72-100 on `v1`. S39 proves later service on `v2`, but it follows the HTTP 504 outage.

For the final proof, keep both versions running and capture a continuous stream of requests that crosses from `v1` to `v2`, including HTTP status, connection errors and timestamps. Verify the nginx configuration inside the running proxy as well as the host file. The current checked-in `bluegreen/nginx.conf` points to Blue. [S14](EVIDENCE.md#s14), [S15](EVIDENCE.md#s15), [S39](EVIDENCE.md#s39)

## Question 3 Canary progression and rollback

The confirmed sample is **90 v1 / 10 v2** out of 100. The subsequent measurement is still 90/10 after the attempted change. The current checked-in `canary/nginx.conf` contains only the Blue upstream: that file state represents the intended rollback configuration, while the screenshot does not prove the runtime had adopted it.

Capture three actual response samples: the initial weighted split, the intended increased v2 share, and an all-v1 result after a complete rollback. Record errors and response times as well as version counts. A printed output label or successful reload command is not a measured traffic result. [S18](EVIDENCE.md#s18), [S19](EVIDENCE.md#s19), [S20](EVIDENCE.md#s20)

## Question 4 GitOps reconciliation

Healthy/Synced status and three ready replicas are present. To directly demonstrate automation, capture the Argo sync/self-heal policy, the desired replica count in Git, an intentional cluster deviation, and Argo restoring the Git-defined state. The existing 1/3 to 3/3 capture shows readiness convergence but not what caused it. [S25](EVIDENCE.md#s25), [S28](EVIDENCE.md#s28)

## Question 5 Secret handling

The supplied evidence shows the credential ID, masking and loading messages, a successful build and Kubernetes Secret injection. Keep real credential values out of screenshots and repository files. No repeat is needed merely to expose the value. [S29-S32](EVIDENCE.md#s29)

## Question 6 Recovery

The restored test file matches the backup checksum. The file timer has whole-second resolution and prints 0 seconds; the endpoint recovery is a separate manual sequence containing HTTP 504 responses. Keep those observations in the report. Define numeric RTO/RPO targets before a new timed recovery run, rather than assigning them retrospectively. [S33-S39](EVIDENCE.md#s33)

## Commit the existing recovery manifests

The repository root checked on **24 November 2026** does not contain `disaster-recovery/`. The documentation ZIP does not recreate those source manifests; use the originals already in your WSL project.

In the Ubuntu WSL terminal:

```bash
cd ~/devops-lab4
ls disaster-recovery/pvc.yaml disaster-recovery/pod.yaml
git status --short
```

If both files are present, add this entry to the existing `.gitignore` if it is not already there:

```gitignore
disaster-recovery/backups/
```

Then stage and inspect the manifests:

```bash
git add .gitignore disaster-recovery/pvc.yaml disaster-recovery/pod.yaml
git diff --cached --stat
```

After checking the staged files, commit and push:

```bash
git commit -m "Add Lab 4 disaster recovery manifests"
git push origin main
```

If you also upload the documentation through the GitHub website, your local branch may need to incorporate that new remote commit before a later push. Keep the local working changes and resolve the branch state normally; a forced push is not needed for this documentation update.

## Check the final GitHub view

- The root README renders and links to the report.
- All screenshot links and seven PDF links open.
- The question order matches the assignment portal.
- The recovery manifests are visible once committed.
- Documentation claims match the captured outputs.

Repository sources checked: [Blue-Green nginx configuration](https://github.com/axdy02/devops-lab4/blob/main/bluegreen/nginx.conf), [Canary nginx configuration](https://github.com/axdy02/devops-lab4/blob/main/canary/nginx.conf), [GitOps deployment](https://github.com/axdy02/devops-lab4/blob/main/gitops/manifests/deployment.yaml), and [repository root](https://github.com/axdy02/devops-lab4).
