# Nutanix NKP CI/CD Demo App
This Flask app can be used to demonstrate NKP's Continuous Delivery. The Flask app displays a web page with the following: 

***Hello from NKP Demo!***

***App Version: <app_version> (Build: <build_version>)***

The *app_version* you manually update in the Dockerfile as part of the demo. The *build_version* is dynamically created from the pipeline using the current date and time. 


## Pre-Demo Steps
1. In NKP create a workspace, project, and CD config for the demo app
2. Add a cluster to the workspace and project 
3. Check the app have been deployed to the cluster. This can be done by going to the Kubernetes Dashboard and finding the deployed pods and service for the app. 


## Demo Steps
1. From NKP go to the Project and Continuous Delivery for the app. 
2. Open the Kubernetes Dashboard for the cluster the app is deployed on, find the apps URL, and open the app. Make a not of the version and build numbers. 
3. In the Dockerfile update 'ENV APP_VERSION=v1.5' to a new version. 
4. Push the changes to GitHub. 
5. In the GitHub repository monitor Actions and wait for the build to finish. 
6. Check the deployments.yaml file to check the 'APP_VERSION' and 'BUILD_VERSION' values have been updated. 
7. Go to https://github.com/pauldjmetsi/nkp-ci-cd-demo/pkgs/container/nkp-ci-cd-demo to check the new package. 
8. Got to back to the Kubernetes Dashboard and wait of the pod to redeploy 
9. Refresh the apps web page and view the changed version and build numbers. 


## Steps to test locally 
Deploy app: 
kubectl apply -f deployment.yaml 

Check deploymant status: 
kubectl rollout status deployment/nkp-demo-app    

As Docker desktop does not have a type LoadBalancer, run the command to port-forward: 
kubectl port-forward svc/nkp-demo-service 8080:80

From a web browser go to: 
http://localhost



