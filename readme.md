# HTTP Proxies Forwarded Headers Propagation demo

## Introduction

This demo aims at showing how nginx ( and proxies in general ) handles and propagates X-Forwarded Headers

Browser -> 433:Proxy1/Nginx -> 80:Proxy2/Nginx -> 5000:Backend

## Build

```
docker-compose build
``` 

## Run

```
docker-compose up
```

## Test

```
https://localhost/api/test
```

Since SSL cert is autosigned then it should be explicitly authorized when browser signals it.