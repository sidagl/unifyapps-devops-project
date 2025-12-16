# unifyapps-devops-project
![CI/CD](https://github.com/sidagl/clouddock-cicd/actions/workflows/deploy.yml/badge.svg)
# Cloud Dock - CICD 🚀

An end-to-end **DevOps CI/CD project** demonstrating how to deploy a Dockerized application on **AWS EC2** using **GitHub Actions**, **Docker Compose**, and **Nginx**.

This project simulates a real-world production deployment pipeline where every push to the `main` branch automatically deploys the latest version of the application to the cloud.

---

## 📌 Project Overview

* Automated CI/CD pipeline triggered on GitHub push
* Dockerized backend application
* Nginx as a reverse proxy
* Deployed on AWS EC2
* Secure secrets handling using GitHub Actions Secrets

**Goal:** Eliminate manual deployment and demonstrate real DevOps workflows used in production environments.

---

## 🏗️ Architecture

```
Developer → GitHub (push)
            ↓
      GitHub Actions (CI/CD)
            ↓ (SSH)
         AWS EC2 Instance
            ↓
     Docker Compose
      ├── Flask App (5000)
      └── Nginx (80)
```

---

## 🛠️ Tech Stack

* **Cloud:** AWS EC2 (Ubuntu)
* **CI/CD:** GitHub Actions
* **Containerization:** Docker, Docker Compose
* **Web Server:** Nginx (Reverse Proxy)
* **Backend:** Python (Flask)
* **Security:** GitHub Secrets, EC2 Security Groups

---

## 📂 Project Structure

```
clouddock-cicd/
├── app/
│   ├── app.py
│   └── requirements.txt
├── docker/
│   └── Dockerfile
├── nginx/
│   └── default.conf
├── docker-compose.yml
├── .github/
│   └── workflows/
│       └── deploy.yml
└── README.md
```

---

## ⚙️ How CI/CD Works

1. Developer pushes code to `main` branch
2. GitHub Actions workflow is triggered
3. Pipeline:

   * Checks out the repository
   * Connects to EC2 via SSH
   * Pulls latest code
   * Runs Docker Compose

```bash
docker-compose down
docker-compose up -d --build
```

4. Application is redeployed automatically with zero manual steps

---

## 🔐 Secrets Used (GitHub Actions)

The following secrets are securely stored in GitHub:

* `EC2_HOST` – Public IP of EC2 instance
* `EC2_USER` – SSH username (ubuntu)
* `EC2_KEY` – Private SSH key (.pem)

No credentials are exposed in the repository.

---

## 🚀 Deployment Verification

After a successful pipeline run, access the application using:

```
http://<EC2_PUBLIC_IP>
```

Expected response:

```json
{
  "env": "production",
  "service": "UnifyApps DevOps Demo",
  "status": "running"
}
```

---

## 🧠 Key Learnings

* End-to-end CI/CD pipeline design
* Secure SSH-based deployments
* Docker multi-container orchestration
* AWS networking and security groups
* Real-world DevOps troubleshooting

---

## 📈 Resume Highlight

```
Built an end-to-end CI/CD pipeline using GitHub Actions to deploy a Dockerized application on AWS EC2 with Nginx reverse proxy and Docker Compose.
```

---

## 🔒 Security Note

For demo purposes, SSH access may be temporarily opened to all IPs. In real-world usage, SSH access should be restricted to trusted IPs or replaced with AWS SSM.

---

## 🧑‍💻 Author

**Siddharth Agarwal**
B.Tech CSE (DevOps) | AWS | Docker | GitHub Actions

---

⭐ If you find this project useful, feel free to star the repository!
