en (enable) - переход в привилегированный режим
conf t (configurate terminal) - режим глобальной конфигурации.


Конфигурация VLAN 

Switch>en
Switch#conf t
Switch(config)#vlan 2
Switch(config-vlan)#name buhgalter
Switch(config-vlan)#interface range fa0/1-5
Switch(config-if-range)#switchport mode access
Switch(config-if-range)#switchport access vlan 2
Switch(config-if-range)#exit