# Basic Python CICD With Google App Engine (GAP) and Google Cloud Build

This repository constains a REST Api solution for managing people. build in python 3.7

### Overview

1. Create Python solution with Flask (v 1.1.2)
1. Create a Google App Engine on Google Cloud Platform to deploy the API.
1. Create a Google Cloud SQL with Postgres to store the data generated by API.
1. Associate APIGEE account with GCP and secure the API with API Proxy.  

  * Create an API Proxy for Generate and access token in OAuth2.
  * Create an API Proxy to secure API People Endpoint.  
  
5. Create a Google Cloud Build to generate the CICD pipelines and link to this GitHub repository.

* In Cloud Builds has been defined a pipeline with two steps (step 1 is for Testing and step 2 for Deploying on Google App Engine)

6. Create SwaggerHub to document the API and represent in a better way its use.

### Deployment Overview

Following the requirements, the files to deploy this solution are three and depends on the way that you want to deploy this. All the mentioned files are in this repository.

- **Github Push (Recommended):**
As I mentioned before Github and GCP are connected by cloud builds. That means you can deploy the solution just pushing your commits in this repository. The related files on this are **Cloudbuild.yaml** and **DockerFile** 

  ```bash
  git add .
  git commit
  git push origin master
  ```
- **Cloud Builds:**
 Using cloud builds you may deploy this. In this case, you will need to use Google Cloud SDK to execute the below command line. The related file is **Cloudbuild.yaml**. However, deploying in this way you will not be pushing your changes on this repository, but at least you will be executing the two-steps pipeline mentioned above (test and deploy).

  ```bash
  gcloud builds submit
  ```
- **App Engine Deploy:**
Finally, you cand deploy this solution with Google App Engine deploy command that you can find when you already have installed the Google Cloud SDK. The file related is **app.yaml**

  ```bash
  gcloud app deploy
  ```
  
