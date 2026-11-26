# DevOps Lab 4 — Advanced Deployment Strategies & Enterprise DevOps

**Environment:** Windows 11, WSL2 Ubuntu, Docker, Jenkins, Kubernetes (Minikube), Argo CD

## 1. Objective

To implement and evaluate advanced DevOps practices, including automated deployment gates, Blue-Green and Canary deployments, GitOps reconciliation, secure secret management, and disaster recovery.

## 2. CI/CD Deployment Gates

A Jenkins pipeline was implemented with automated unit and integration tests.

- Three unit tests and three integration tests were executed.
- Successful tests allowed the deployment approval stage to execute.
- An intentionally failing test blocked the deployment approval stage.
- The pipeline was restored and executed successfully.

**Result:** Automated test gates successfully prevented progression when tests failed. The deployment gate provided approval rather than executing a production deployment.

## 3. Blue-Green Deployment

Two versions of the Flask application were deployed using Docker Compose.

- Blue environment: application version v1.
- Green environment: application version v2.
- Nginx was used as a reverse proxy to switch application traffic.
- Application responses were verified after switching environments.

**Advantages:** Rapid rollback, isolated release validation, and potentially low-downtime deployment.

**Limitations:** Duplicate infrastructure requirements, additional resource usage, and potential database compatibility issues.

## 4. Canary Deployment

Weighted Nginx upstreams were configured to progressively route traffic to the new application version.

- Initial traffic allocation: 90% Blue and 10% Green.
- Increased Green traffic allocation to 30%.
- Responses were sampled to observe traffic distribution.
- Rollback was demonstrated by routing all traffic back to Blue.

**Advantages:** Reduced deployment risk, gradual exposure, and easier detection of release problems.

**Limitations:** Requires traffic management, monitoring, rollback criteria, and careful interpretation of performance metrics.

## 5. GitOps Using Argo CD

A local Kubernetes cluster was created using Minikube v1.35.0.

Argo CD was installed and connected to the GitHub repository as the desired configuration source.

- Kubernetes Deployment and Service manifests were stored in Git.
- Argo CD deployed the application with two replicas.
- A Git commit changed the desired replica count from two to three.
- Argo CD synchronized the updated configuration.
- A manual change to the running deployment was automatically corrected.

**Result:** GitOps synchronization and self-healing were demonstrated successfully.

## 6. Secure Secret Management

Two approaches were implemented.

**Jenkins Credentials**

- A secret-text credential was stored in Jenkins.
- The pipeline accessed it through `withCredentials`.
- Jenkins enabled credential masking.
- Validation succeeded without printing the credential value.

**Kubernetes Secrets**

- A demo Secret was created inside Kubernetes.
- A Pod consumed the Secret using `secretKeyRef`.
- Container logs confirmed successful injection without revealing the secret value.

**Security considerations:** Use least-privilege access, avoid committing credentials to Git, rotate secrets, and use an external secret manager for production environments.

## 7. Disaster Recovery

A Kubernetes PersistentVolumeClaim was provisioned and used to store sample application data.

The recovery procedure included:

1. Writing and verifying the original data.
2. Creating a local backup.
3. Simulating accidental file deletion.
4. Restoring the file from the backup.
5. Comparing SHA-256 checksums.

The restored file matched the backup exactly.

**Recovery measurement:** The demonstration reported 0 seconds using whole-second timestamps. This indicates insufficient timer resolution for a precise duration measurement, not instantaneous recovery.

**RTO:** Maximum acceptable recovery time.

**RPO:** Maximum acceptable data loss measured in time.

A separate manual failover demonstration stopped the Blue application and redirected traffic to Green. Nginx initially returned HTTP 504. After the proxy configuration was corrected and its container recreated, the application returned HTTP 200 with version v2.

This demonstrated successful manual recovery, but not automatic or uninterrupted failover.

## 8. Strategy Comparison

| Strategy | Primary Benefit | Main Risk | Suitable Use |
|---|---|---|---|
| Blue-Green | Fast switching and rollback | Duplicate infrastructure cost | Major application releases |
| Canary | Gradual exposure | Monitoring and routing complexity | Risk-sensitive releases |
| GitOps | Declarative, aud
