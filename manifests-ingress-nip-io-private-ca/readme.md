# Setup Steps

## Create the Root CA Certificate, Issuer, and Certificate
```
kubectl apply -f certificates.yaml
```

## Create App with Ingress
```
kubectl apply -f deployment.yaml
```

## Get the Root CA Certificate
```
$certBase64 = kubectl get secret cicd-demo-root-ca-secret -n cicd-demo -o jsonpath='{.data.tls\.crt}'
$certText = [System.Text.Encoding]::UTF8.GetString([System.Convert]::FromBase64String($certBase64))
$certText | Out-File -FilePath "$env:USERPROFILE\Desktop\cicd-demo-root-ca.crt" -Encoding ascii
```

## Install the Root CA Certificate on your local machine (Windows)
1. Double click on the file you just created
2. Click on the Install Certificate button
3. Click on the Local Machine button
4. Select the option to Place all certificates in the following store
5. Browse and select Trusted Root Certification Authorities
6. Click Finish
