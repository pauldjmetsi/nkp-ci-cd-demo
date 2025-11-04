# Nutanix NKP CI/CD Demo App

# 

## Steps to test locally 
Deploy app: kubectl apply -f deployment.yaml 
Check deploymant status: kubectl rollout status deployment/nkp-demo-app    
As Docker desktop does not have a type LoadBalancer, run the command to port-forward: kubectl port-forward svc/nkp-demo-service 8080:80
From a web browser go to: http://localhost



