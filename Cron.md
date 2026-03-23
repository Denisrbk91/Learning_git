`cron` — это служба (демон), которая **по расписанию запускает команды/скрипты**. Расписание хранится в “crontab” (таблица заданий). Каждую минуту cron просыпается, сверяет расписание и запускает нужное.

crontab -e # редактировать задания текущего юзера  
crontab -l # показать задания  
crontab -r # удалить все задания  
sudo crontab -e # задания root

Формат 
MIN HOUR DOM MON DOW command

`*` — любой
`*/5` — каждые 5
`1-5` — диапазон
`1,3,7` — список

Пример 
Каждый день в 02.00
0 2 * * * /usr/local/bin/backup.sh >/var/log/backup.log 2>&1

Каждые 5 минут
*/5 * * * * /usr/local/bin/check.sh >/var/log/check.log 2>&1

Каждый понедельник в 09.30
30 9 * * 1 /usr/local/bin/report.sh >/var/log/report.log 2>&1

Пиши **полные пути** к командам/скриптам (`/usr/bin/python3`)
Всегда логируй: `>/path/log 2>&1`
Cron-сервис: `systemctl status cron` (Ubuntu) / `systemctl status crond` (RHEL)