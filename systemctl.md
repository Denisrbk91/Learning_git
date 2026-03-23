systemctl команда (что делаем) объект (над чем делаем) 
ПРИМЕР - systemctl status sshd

systemctl disable/enable sshd - отключение службы (даже при рестарте изменения сохранятся)
systemctl list-units --all   : список всех юнитов(служб?)
systemctl lis-unit-file  вывод всех установленных в системе служб

journalctl -u XXX   посмотреть логи конкретного сервиса

Посмотреть последние 200 строк
journalctl -u nginx -n 200

systemctl enable --now XXX - включить автозапуск и сразу запустить сервис