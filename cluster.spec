metadata:
  creationTimestamp: "2019-12-05T10:28:02Z"
  name: deploy.k8s.local
spec:
  api:
    loadBalancer:
      crossZoneLoadBalancing: false
      type: Public
  authorization:
    rbac: {}
  channel: stable
  cloudProvider: aws
  clusterDNSDomain: cluster.local
  configBase: s3://test-case-kube-sigma/deploy.k8s.local
  configStore: s3://test-case-kube-sigma/deploy.k8s.local
  docker:
    ipMasq: false
    ipTables: false
    logDriver: json-file
    logLevel: warn
    logOpt:
    - max-size=10m
    - max-file=5
    storage: overlay2,overlay,aufs
    version: 18.06.3
  etcdClusters:
  - backups:
      backupStore: s3://test-case-kube-sigma/deploy.k8s.local/backups/etcd/main
    cpuRequest: 200m
    enableEtcdTLS: true
    enableTLSAuth: true
    etcdMembers:
    - instanceGroup: master-us-east-2b
      name: b
    manager: {}
    memoryRequest: 100Mi
    name: main
    provider: Manager
    version: 3.3.10
  - backups:
      backupStore: s3://test-case-kube-sigma/deploy.k8s.local/backups/etcd/events
    cpuRequest: 100m
    enableEtcdTLS: true
    enableTLSAuth: true
    etcdMembers:
    - instanceGroup: master-us-east-2b
      name: b
    manager: {}
    memoryRequest: 100Mi
    name: events
    provider: Manager
    version: 3.3.10
  iam:
    allowContainerRegistry: true
    legacy: false
  keyStore: s3://test-case-kube-sigma/deploy.k8s.local/pki
  kubeAPIServer:
    allowPrivileged: true
    anonymousAuth: false
    apiServerCount: 1
    authorizationMode: RBAC
    bindAddress: 0.0.0.0
    cloudProvider: aws
    enableAdmissionPlugins:
    - NamespaceLifecycle
    - LimitRanger
    - ServiceAccount
    - PersistentVolumeLabel
    - DefaultStorageClass
    - DefaultTolerationSeconds
    - MutatingAdmissionWebhook
    - ValidatingAdmissionWebhook
    - NodeRestriction
    - ResourceQuota
    etcdServers:
    - http://127.0.0.1:4001
    etcdServersOverrides:
    - /events#http://127.0.0.1:4002
    image: k8s.gcr.io/kube-apiserver:v1.15.5
    insecureBindAddress: 127.0.0.1
    insecurePort: 8080
    kubeletPreferredAddressTypes:
    - InternalIP
    - Hostname
    - ExternalIP
    logLevel: 2
    requestheaderAllowedNames:
    - aggregator
    requestheaderExtraHeaderPrefixes:
    - X-Remote-Extra-
    requestheaderGroupHeaders:
    - X-Remote-Group
    requestheaderUsernameHeaders:
    - X-Remote-User
    securePort: 443
    serviceClusterIPRange: 100.64.0.0/13
    storageBackend: etcd3
  kubeControllerManager:
    allocateNodeCIDRs: true
    attachDetachReconcileSyncPeriod: 1m0s
    cloudProvider: aws
    clusterCIDR: 100.96.0.0/11
    clusterName: deploy.k8s.local
    configureCloudRoutes: true
    image: k8s.gcr.io/kube-controller-manager:v1.15.5
    leaderElection:
      leaderElect: true
    logLevel: 2
    useServiceAccountCredentials: true
  kubeDNS:
    cacheMaxConcurrent: 150
    cacheMaxSize: 1000
    cpuRequest: 100m
    domain: cluster.local
    memoryLimit: 170Mi
    memoryRequest: 70Mi
    replicas: 2
    serverIP: 100.64.0.10
  kubeProxy:
    clusterCIDR: 100.96.0.0/11
    cpuRequest: 100m
    hostnameOverride: '@aws'
    image: k8s.gcr.io/kube-proxy:v1.15.5
    logLevel: 2
  kubeScheduler:
    image: k8s.gcr.io/kube-scheduler:v1.15.5
    leaderElection:
      leaderElect: true
    logLevel: 2
  kubelet:
    anonymousAuth: false
    cgroupRoot: /
    cloudProvider: aws
    clusterDNS: 100.64.0.10
    clusterDomain: cluster.local
    enableDebuggingHandlers: true
    evictionHard: memory.available<100Mi,nodefs.available<10%,nodefs.inodesFree<5%,imagefs.available<10%,imagefs.inodesFree<5%
    featureGates:
      ExperimentalCriticalPodAnnotation: "true"
    hostnameOverride: '@aws'
    kubeconfigPath: /var/lib/kubelet/kubeconfig
    logLevel: 2
    networkPluginMTU: 9001
    networkPluginName: kubenet
    nonMasqueradeCIDR: 100.64.0.0/10
    podInfraContainerImage: k8s.gcr.io/pause-amd64:3.0
    podManifestPath: /etc/kubernetes/manifests
  kubernetesApiAccess:
  - 0.0.0.0/0
  kubernetesVersion: 1.15.5
  masterInternalName: api.internal.deploy.k8s.local
  masterKubelet:
    anonymousAuth: false
    cgroupRoot: /
    cloudProvider: aws
    clusterDNS: 100.64.0.10
    clusterDomain: cluster.local
    enableDebuggingHandlers: true
    evictionHard: memory.available<100Mi,nodefs.available<10%,nodefs.inodesFree<5%,imagefs.available<10%,imagefs.inodesFree<5%
    featureGates:
      ExperimentalCriticalPodAnnotation: "true"
    hostnameOverride: '@aws'
    kubeconfigPath: /var/lib/kubelet/kubeconfig
    logLevel: 2
    networkPluginMTU: 9001
    networkPluginName: kubenet
    nonMasqueradeCIDR: 100.64.0.0/10
    podInfraContainerImage: k8s.gcr.io/pause-amd64:3.0
    podManifestPath: /etc/kubernetes/manifests
    registerSchedulable: false
  masterPublicName: api.deploy.k8s.local
  networkCIDR: 172.20.0.0/16
  networking:
    kubenet: {}
  nonMasqueradeCIDR: 100.64.0.0/10
  secretStore: s3://test-case-kube-sigma/deploy.k8s.local/secrets
  serviceClusterIPRange: 100.64.0.0/13
  sshAccess:
  - 0.0.0.0/0
  subnets:
  - cidr: 172.20.32.0/19
    name: us-east-2b
    type: Public
    zone: us-east-2b
  topology:
    dns:
      type: Public
    masters: public
    nodes: public
