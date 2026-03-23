## ![[Практика из РОАДМАПА.pdf]]0) Подготовка: сквозной учебный проект + стенд

Смысл (как на доске): многие практические пункты формата “взять приложение…” лучше делать **одним** проектом и протащить его через все этапы.

1. Заведи репозиторий (GitHub/GitLab) и структуру:
    

- `app/` — код приложения
    
- `deploy/linux/` — запуск “на голом Linux” + systemd unit + nginx конфиг
    
- `deploy/docker/` — Dockerfile + compose
    
- `deploy/cicd/` — `.gitlab-ci.yml` (и/или Jenkinsfile)
    
- `deploy/ansible/` — inventory + playbooks + roles
    
- `deploy/k8s/` — манифесты + helm chart
    
- `observability/` — prometheus/grafana + (loki/elk)
    

2. Выбери простое приложение:
    

- минимально: HTTP-сервис на **Python** + PostgreSQL (опционально фронт).
    
- как на доске: можно “попросить нейронку сгенерировать Frontend + Backend + БД”, и дальше доводить руками.
    

3. Подними 1–2 VM:
    

- одна — “сервер” для деплоя по SSH,
    
- вторая — “песочница” для экспериментов (можно локально на VirtualBox/VMware/Proxmox).
    

---

## 1) Git

**Почему первым (по доске):** конфиги/манифесты/пайплайны должны **версионироваться**, и неважно GitHub/GitLab/Bitbucket — в основе везде git.

### Теория

1. База:
    

- `git init`, `git add`, `git commit`, `git push`, `git pull`
    

2. Команды, которые важно понимать:
    

- `git checkout`, `git merge`, `git rebase`, `git fetch`, `git revert`, `git diff`, `git clone`
    

3. Стратегии ветвления:
    

- GitFlow
    
- GitHub Flow, GitLab Flow, Trunk-Based
    

4. Что такое стратегия ветвления: какие ветки “живут всегда”, правила, когда и как сливать.
    

### Практика

1. Репозиторий под сквозной проект.
    
2. Ветки + MR/PR:
    

- сделать фичу в отдельной ветке,
    
- открыть MR,
    
- словить merge conflict и решить.
    

3. Отдельно потренировать:
    

- перенос коммитов между ветками (rebase/cherry-pick),
    
- аккуратную работу с историей (rebase + `--force-with-lease` в тестовом репо).
    

### Собесы (по доске)

Git спрашивают редко, но если спрашивают — почти всегда:

- как перенести коммиты из одной ветки в другую;
    
- что такое merge conflict и причины;
    
- как работает `git pull` “под капотом”.
    

---

## 2) Linux

**Почему так рано (по доске):** “везде Linux: сервера, виртуалки, Kubernetes”.

### Как учить (практика-основа)

1. Лучше всего — поставить Linux второй системой или хотя бы развернуть на VM.
    
2. Дальше — реально пользоваться регулярно.
    

### Теория (ключевые блоки из доски)

- загрузка и инициализация
    
- файловая система
    
- права и пользователи
    
- процессы и службы, сигналы и состояния процессов
    
- bash-скрипты
    
- работа с сетью
    
- nginx
    
- ресурсы и железо
    

**Навигация и терминал (по доске):**

- работа с файлами: `find`, `locate`, `tree`, `ln`, `stat`, `file`
    
- потоки/перенаправления: `stdin`, `stdout`, `stderr`, пайпы
    
- `profile`, `.profile`
    
- работа с текстом: `grep`, `awk`, `sed`, `cut`, `sort`, `uniq`, `wc`, `xargs` (отмечено как супер для дебага по логам)
    
- bash-скриптинг: условия, циклы, функции, exit-коды
    
- SSH: ключи, `ssh-keygen`, `ssh-copy-id`, ssh-config
    

**Процессы/производительность/логи (из доски):**

- псевдофайловая система, `ps aux`
    
- `top/htop`: понимать `load average`, `us`, `sy`, `wa`, `si`, `id` и т.д.
    
- сигналы (на доске: “64 штуки”, знать основные)
    
- файловые системы, `mount`, `/etc/fstab`
    
- глубокая диагностика:
    
    - `vmstat`, `iostat`, `sar`, `dstat`, `pidstat`
        
    - память: RSS/VSZ/shared, page cache, `free -h` (как читать `available`)
        
    - swap
        
    - сеть: `ss`, `netstat`, `iftop`, `nload`
        
    - `perf top`, `perf record`, flamegraphs
        
    - логирование: `journalctl`, syslog, `/var/log`
        

**Продвинутый фундамент (из доски):**

- `nohup`, `disown`, `screen`, `tmux`
    
- cgroups (прямой мост к Docker/K8s)
    
- namespaces (изоляция)
    
- systemd углублённо: зависимости юнитов, timers (замена cron), `journalctl` фильтрация, написание unit-файлов
    
- `strace/ltrace`
    

### Практика (что сделать руками)

1. “Голое” приложение без контейнеров:
    

- запустить приложение на Linux руками.
    

2. Первичная настройка сервера (по доске):
    

- создать пользователя
    
- sudo
    
- SSH по ключам
    
- отключить вход по паролю и root-логин
    
- базовый firewall (`ufw` или `iptables`)
    

3. Systemd:
    

- написать свой systemd-юнит.
    

4. Сильное упражнение из доски:
    

- взять любой скрипт (хоть простой HTTP-сервер на Python) и оформить как сервис:
    
    - автозапуск
        
    - рестарт при падении
        
    - лимиты памяти через cgroups
        
    - проверить, что после `kill -9` сервис поднимается сам
        

5. Nginx:
    

- поднять nginx (как reverse proxy).
    

6. Диски и ФС:
    

- смонтировать и настроить автоподключение через `/etc/fstab`.
    

### Собесы (вопросы с доски)

- Что такое Load Average?
    
- Что такое inodes?
    
- Zombie-процесс?
    
- “No space left on device”, но место есть — почему?
    
- Загрузка Linux от питания до приглашения
    
- Какие сигналы процессов знаешь?
    
- Права `755` для директории
    
- LVM и зачем он нужен
    

---

## 3) Сети

### Теория (по доске)

1. OSI: все 7 уровней, особый фокус на 3/4/7.
    
2. Протоколы: TCP/UDP, ICMP, HTTP, DNS, TLS/SSL, SSH, ARP.
    
3. Утилиты траблшутинга:
    

- `ping`, `traceroute/mtr`, `netstat/ss`, `telnet/curl`, `nc`, `nmap`, `tcpdump`, Wireshark, `iftop`, `iptables`
    

4. Балансировщики: Nginx, HAProxy.
    

### Практика (чтобы “встало”)

1. Разобрать путь запроса: DNS → TCP/TLS → HTTP → приложение.
    
2. Снять `tcpdump` и увидеть handshake/HTTP.
    
3. Поднять Nginx как reverse proxy, затем добавить второй инстанс приложения и настроить балансировку.
    

### Собесы (по доске)

- Что происходит при вводе URL и Enter?
    
- TLS Handshake
    
- Маска подсети
    
- Уровни OSI
    
- TCP vs UDP
    
- Как работает DNS
    

---

## 4) Docker

**Логика блока (по доске):** контейнеры везде, но не только Docker (Podman/Buildah/containerd). Docker нужен, чтобы понять концепт и “почему так”.

### Теория

1. Образы и контейнеры.
    
2. Архитектура:
    

- Docker Daemon
    
- Docker Client (CLI)
    
- Docker API
    

3. Команды (по доске):
    

- `docker build`, `docker images`, `docker pull`, `docker push`, `docker tag`, `docker history`
    
- `docker run`, `docker ps`, `docker stop`, `docker logs`, `docker exec`
    
- `docker network`
    

4. Dockerfile:
    

- уметь написать + знать директивы:
    
    - `FROM`, `RUN`, `COPY`, `ADD`, `WORKDIR`, `ENV`, `ARG`, `EXPOSE`, `CMD`, `ENTRYPOINT`, `USER`
        
- разница `CMD/ENTRYPOINT`, `COPY/ADD`
    
- multi-stage build
    
- best practices (в т.ч. как уменьшать размер образа)
    

5. Что учитывается при сборке (build context) → на практике `.dockerignore`.
    
6. Тегирование/версионирование образов и нейминг.
    
7. Docker networking:
    

- типы сетей: `bridge`, `host`, `none`, `overlay`, `macvlan`
    

8. Docker Compose:
    

- описание связки “приложение+БД+кэш+nginx+мониторинг”
    
- поднятие/гашение одной командой
    

### Практика (сквозной проект)

1. Взять приложение из Linux-практики → контейнеризировать → поднять → проверить.
    
2. Nginx в контейнере (по доске):
    

- не просто `docker run nginx`,
    
- примонтировать свой `nginx.conf` (bind mount),
    
- отдавать свою статику,
    
- проброс портов.
    

3. Compose:
    

- завернуть приложение в `docker compose`,
    
- проверить корректность работы всех контейнеров.
    

4. Мониторинг в compose (прямо с доски, очень полезно):
    

- Prometheus + Grafana + Node Exporter
    
- - опционально cAdvisor
        

5. Эксперименты (по доске):
    

- быстро поднимать/ломать/тестировать (на фантазию, нейронки в помощь).
    

### Собесы (по доске)

Docker/контейнеры сейчас спрашивают реже, но если спрашивают:

- контейнеризация vs виртуализация
    
- cgroups/namespaces
    
- multi-stage build
    
- best practices
    
- Dockerfile нюансы (CMD/ENTRYPOINT, COPY/ADD)
    
- сеть Docker
    

---

## 5) CI/CD

### Теория (вопросы/темы с доски)

- что такое CI / CD
    
- принципы построения CI/CD
    
- стратегии разработки (GitFlow и подобные)
    
- интеграции в CI/CD (Docker, Ansible)
    
- GitOps
    
- что такое деплой
    

### Инструменты (по доске)

- GitLab CI и Jenkins:
    
    - Jenkins часто в старых/закрытых контурах
        
    - GitLab CI — активно растёт
        
- Практику лучше делать на GitLab CI (так и сказано на доске).
    

### GitLab CI — что знать

- `pipeline`, `stage`, `job`
    
- `.gitlab-ci.yml` (build/test/deploy)
    
- `only/rules`
    
- `variables` + CI/CD Variables в настройках проекта (секреты)
    
- `artifacts`, `cache`
    
- продвинуто (любят спрашивать):
    
    - `needs`
        
    - `extends` + YAML-якоря
        
    - `include`
        
    - `trigger`
        
    - GitLab Runner + executor’ы (shell/docker/kubernetes)
        

### Jenkins — что знать

- Master + Agent
    
- triggers (manual/webhook/schedule)
    
- Jenkinsfile declarative:
    
    - `pipeline`, `agent`, `stages/stage/steps`
        
    - `post`
        
    - `environment`
        
    - `Credentials`
        
    - `parameters`
        
    - webhook из GitLab/GitHub
        
- продвинуто:
    
    - Groovy scripted pipelines
        
    - Shared Libraries
        
    - parallel stages
        
    - `when`, `input`
        
    - multibranch
        
    - docker agent
        

### Практика (по доске)

1. Простой пайплайн (3 стадии):
    

- Build: собрать Docker-образ из Dockerfile
    
- Test: линтер (`flake8` / `eslint`)
    
- Deploy: SSH на сервер
    

2. Пайплайн с окружениями:
    

- dev: авто по пушу в ветку
    
- staging: авто по merge в `main`
    
- prod: только manual
    
- артефакты между стейджами
    
- секреты через CI/CD Settings Variables
    
- кэш зависимостей
    

3. Registry-часть (из доски):
    

- build + push образа в GitLab Registry
    
- environments
    
- `when: manual` на деплой
    

### Собесы (по доске)

- “Как бы ты построил идеальный пайплайн?”
    
- частые вопросы про `extends/include` в GitLab CI
    
- CI/CD принципы + стратегии ветвления + GitOps
    

---

## 6) Ansible

**По доске:** можно начинать раньше, но “удобнее применять после CI/CD”.

### Теория (по доске)

- инструмент управления конфигурациями (управляющая машина → целевые хосты)
    
- agentless (SSH + Python)
    
- декларативность
    
- идемпотентность
    
- inventory (INI/YAML)
    
- модули: `apt`, `yum`, `copy`, `template`, `file`, `service`, `user`, `docker`
    
- ad-hoc (самая база)
    
- playbook (как bash-скрипт, но декларативный/идемпотентный)
    
- роли (nginx/postgresql/мониторинг; в компаниях всё на ролях)
    
- дополнительно: `ansible vault`
    

### Практика

- ad-hoc команды на VM
    
- написать playbook (подготовить сервер под приложение)
    
- написать role (вынести конфигурации в роли)
    
- спрятать секреты в ansible vault (опционально)
    

### Собесы (по доске)

Спрашивают нечасто, но типично:

- что такое playbook
    
- что такое роли
    
- приоритеты переменных
    
- Handler
    
- идемпотентность
    

---

## 7) Kubernetes

**По доске:** самый большой и важный блок; на собесах бывает “99% вопросов”.

### Фундамент

1. Поставить локальный кластер:
    

- Minikube / Kind / k3d
    

2. Сразу учить `kubectl`.
    

### Архитектура (по доске)

- Control Plane: API Server, etcd, Scheduler, Controller manager, Cloud Controller manager
    
- Worker node: kubelet, container runtime, kube-proxy
    

### Основные сущности (по доске)

Pod, Deployment, DaemonSet, StatefulSet, ConfigMap, Secret, Job, CronJob

### Сеть

- Service / Ingress (манифестами)
    
- “под капотом”: CNI, kube-proxy, CoreDNS, сеть на уровне нод
    

### Хранилище

- PV / PVC / StorageClass
    
- access modes
    

### Продвинутые вещи (база из доски)

- RBAC
    
- HPA
    

### Helm

- Helm = пакетный менеджер Kubernetes (как apt), используется почти везде.
    

### Развертывание кластера (по доске)

- kubeadm
    
- kubespray
    
- managed Kubernetes
    

### Практика (максимально конкретно по доске)

1. Манифесты руками (без Helm):
    

- Deployment + Service + ConfigMap
    
- обновить image → посмотреть RollingUpdate → откат
    
- scale 5 → 1
    

2. Probes:
    

- добавить liveness/readiness
    
- сломать readiness → pod выпадет из Service, но не рестарт
    
- сломать liveness → увидеть рестарт
    

3. Helm chart:
    

- завернуть манифесты в chart
    
- вынести в values: replicas, image tag, resource limits, ingress host
    
- сделать values-dev.yaml и values-prod.yaml
    
- задеплоить в два namespace через Helm
    

4. “Полный стек” по смыслу доски:
    

- Frontend + Backend + PostgreSQL (БД можно не тащить в кластер)
    

### Собесы (вопросы с доски)

- Deployment vs StatefulSet vs DaemonSet
    
- архитектура Kubernetes
    
- типы Service
    
- почему pod, а не контейнер
    
- Ingress vs Ingress Controller
    
- HPA
    
- Affinity/Anti-Affinity
    

**Пример из доски (GPU-ноды):**  
Чтобы pod попал только на GPU-ноду:

- taint на GPU-ноды
    
- toleration у pod
    
- node affinity (или nodeSelector) по лейблу GPU-ноды
    

### Что дальше (развилка с доски)

- операторы
    
- ServiceMesh (Istio/Linkerd)
    
- бэкапирование etcd
    
- GitOps (ArgoCD/Flux)
    
- multi-cluster
    

---

## 8) Остальное (полезно, но вторым приоритетом)

Как на доске: “всё полезное, но не приоритетное; ниже — ниже приоритет”.

### Базы

- `pg_hba.conf`, `postgresql.conf`
    
- бэкап/restore
    
- репликация
    
- мониторинг баз
    
- базовый SQL: SELECT/INSERT/CREATE TABLE/GRANT  
    (по доске: DevOps чаще администрирует/восстанавливает/мониторит, чем пишет SQL)
    

### Мониторинг

- Prometheus, Grafana
    
- 4 “золотых сигнала”
    
- USE (cpu/ram/диск/сеть)
    
- RED (rate/errors/duration)  
    Практика: compose-стек Prometheus+Grafana+Node Exporter (+ cAdvisor)
    

### Логи

- ELK или Loki+Grafana
    
- источники: файлы серверов, stdout k8s-подов
    
- сборщики: Fluentd, Filebeat, Fluent Bit  
    Практика: поднять ELK/Loki и “потыкаться”
    

### Облака

- IaaS/PaaS/SaaS
    
- VM + SSH
    
- VPC/подсети/secgroups
    
- S3
    
- managed сервисы (постгре/кубер и т.д.)
    

### Terraform

**Концепции (с доски):** Provider, Resource, State, Plan, Module, Backend, Apply  
Практика: описать VM+сеть, настроить backend для state, попробовать модульность

### Vault

- отдельный блок секретов (параллельно: ansible vault как быстрый старт)
    

### GitOps: ArgoCD

- Git — источник правды
    
- поставить ArgoCD, подключить репу, задеплоить
    
- App of Apps, helm через Argo (если зайдёт — углубляться)
    

### Очереди сообщений

**Концепции (с доски):** брокер, топик, партиции, оффсеты, продюсеры, консьюмеры, репликация, consumer group

### Архитектура

- базово понимать связки сервисов (frontend/backend/DB) и что где держать (в кластере/в managed и т.п.)