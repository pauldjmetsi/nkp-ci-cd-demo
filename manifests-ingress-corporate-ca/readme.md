# Setup Steps

## Create secret with the Customer's CA certificate/key
```
kubectl create secret tls customer-ca-secret \
  --cert=corporate-root.crt \
  --key=corporate-root.key \
  -n cert-manager # Best practice to put the secret where cert-manager lives
```

## Important Info

1. The CA Secret: The customer-ca-secret (containing the customer's Root CA files) must be in the same namespace as cert-manager (usually the cert-manager or kommander namespace).

2. The App Secret: The cicd-demo-tls secret will be automatically created by cert-manager in your cicd-demo namespace. You don't need to do anything for this; it happens magically as soon as you apply that YAML.

## Verify Certificate
Run the following command to see the details of the certificate:
```
kubectl describe certificate cicd-demo-tls -n cicd-demo
```
If you see "Certificate issued successfully", then it has worked. 

---
---
---


## Troubleshooting

1. If you ever apply the Ingress and the certificate just sits there as Ready: False, the very first thing to check is if the ClusterIssuer is happy. You can check its status with:
```
kubectl describe clusterissuer corporate-ca-issuer
```
If the secret is in the wrong namespace, the "Events" section at the bottom of that command will tell you exactly that.


## Questions?

### How do I make sure a user stays on the same pod for their whole session?
If the customer scales your demo app to 3 replicas, they might ask: "How do I make sure a user stays on the same pod for their whole session?"

The Answer: Add a Traefik annotation for "Sticky Sessions."
```
annotations:
  traefik.ingress.kubernetes.io/service.sticky.cookie: "true"
```

### Middlewares
Middlewares are Traefik's way of performing "actions" on a request before it reaches your application. Think of them as a filter or a security checkpoint sitting between the internet and your pod.

How Middlewares Work
In a standard Kubernetes Ingress, you are usually limited to simple routing. With Traefik Middlewares, you can add complex logic without changing a single line of your application's code.

**Example: Adding an IP Whitelist**
If a customer says, "I only want people on our corporate VPN to access this demo app," you would use an IPWhiteList middleware.

Step 1: Create the Middleware object
```
apiVersion: traefik.io/v1alpha1
kind: Middleware
metadata:
  name: corporate-ip-whitelist
  namespace: cicd-demo
spec:
  ipWhiteList:
    sourceRange:
      - 10.0.0.0/8    # Internal range
      - 192.168.1.0/24 # Office range
```

**Step 2: Attach it to your Ingress**
You simply add an annotation to your existing Ingress. Note the format: namespace-name@kubernetescrd.
```
metadata:
  annotations:
    kubernetes.io/ingress.class: "kommander-traefik"
    # Attach the middleware here
    traefik.ingress.kubernetes.io/router.middlewares: "cicd-demo-corporate-ip-whitelist@kubernetescrd"
```

**3 Middlewares Customers Ask For Most:**

Middleware Type: 

- **BasicAuth:** - **Use Case:** Adding a quick username/password prompt. |  **Customer Value:** "I don't want the public seeing my dev site."
- **RateLimit:** - **Use Case:** Preventing a single user from overwhelming the app. |  **Customer Value:** ""Stop brute-force attacks or accidental loops.""
- **Header Modifications:** - **Use Case:** Adding custom security headers like X-Frame-Options. |  **Customer Value:** ""Our security audit says we need these headers."

