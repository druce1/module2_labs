from task_1 import IP_packet  # Класс №1 "IP_packet"


def test_ip_packet():
    # Проверка корректного создания пакета
    try:
        packet = IP_packet(1400, 64)
        print("Пакет создан успешно:", packet.packet_size, packet.ttl)
    except Exception as e:
        print("Ошибка при создании пакета:", e)

    # Проверка пакета большого размера (больше 1500 байт)
    try:
        packet = IP_packet(1600, 64)
    except ValueError as e:
        print("Создадим пакет больше 1500 байт:", e)

    # Проверка некорректного значения TTL (меньше или равно 1)
    try:
        packet = IP_packet(1400, 1)
    except ValueError as e:
        print("Создадим пакет с TTL <= 1:", e)

    # Проверка работы метода forward_packet с корректным TTL
    try:
        packet = IP_packet(1400, 64)
        result = packet.forward_packet()
        print("Результат forward_packet с корректным TTL:", result)
    except Exception as e:
        print("Ошибка при вызове forward_packet с корректным TTL:", e)

    # Проверка работы метода forward_packet с некорректным TTL (1)
    try:
        packet = IP_packet(1400, 1)
        result = packet.forward_packet()
        print("Результат forward_packet с TTL=1:", result)
    except Exception as e:
        print("Ошибка при вызове forward_packet с TTL=1:", e)

    # Проверка уменьшения TTL до нуля (должна быть ошибка)
    try:
        packet = IP_packet(1400, 2)
        packet.decrease_ttl(2)  # уменьшаем TTL до 0
    except ValueError as e:
        print("Уменьшим TTL до 0:", e)

    # Проверка уменьшения TTL с некорректным значением decrease_by (отрицательное число)
    try:
        packet = IP_packet(1400, 64)
        packet.decrease_ttl(-1)
    except ValueError as e:
        print("Уменьшим TTL на отрицательное число:", e)

    # Проверка уменьшения TTL с некорректным типом decrease_by (не целое число)
    try:
        packet = IP_packet(1400, 64)
        packet.decrease_ttl("abc")
    except TypeError as e:
        print("Уменьшим TTL на другой тип данных:", e)


if __name__ == "__main__":
    test_ip_packet()

# Класс №2 "Switch"

from task_1 import NetworkSwitch

def test_network_switch():
    # Проверка корректного создания объекта NetworkSwitch
    try:
        switch = NetworkSwitch(24, 1000)
        print("Сетевой коммутатор успешно создан:", switch.port_count, switch.port_speed)
    except Exception as e:
        print("Ошибка при создании сетевого коммутатора:", e)

    # Проверка некорректного количества портов (не кратно двум)
    try:
        switch = NetworkSwitch(25, 1000)
    except ValueError as e:
        print("Зададим количество портов, которое не кратно двум:", e)

    # Проверка некорректного количества портов (вне диапазона)
    try:
        switch = NetworkSwitch(50, 1000)
    except ValueError as e:
        print("Зададим количество портов больше 48:", e)

    # Проверка некорректной скорости порта
    try:
        switch = NetworkSwitch(24, 500)
    except ValueError as e:
        print("Зададим недопустимую скорость порта:", e)

    # Проверка метода check_ports_status
    try:
        switch = NetworkSwitch(8, 100)
        ports_status = switch.check_ports_status()
        print("Состояние портов:", ports_status)
    except Exception as e:
        print("Ошибка при проверке состояния портов:", e)

    # Проверка метода update_port_speed с корректным значением
    try:
        switch = NetworkSwitch(8, 100)
        switch.update_port_speed(10000)
        print("Скорость портов успешно обновлена:", switch.port_speed)
    except ValueError as e:
        print("Ошибка при обновлении скорости портов:", e)

    # Проверка метода update_port_speed с некорректным значением
    try:
        switch = NetworkSwitch(8, 100)
        switch.update_port_speed(500)
    except ValueError as e:
        print("Установим недопустимую скорость порта:", e)

    # Проверка метода calculate_total_bandwidth
    try:
        switch = NetworkSwitch(16, 1000)
        total_bandwidth = switch.calculate_total_bandwidth()
        print("Общая пропускная способность:", total_bandwidth, "Мбит/с")
    except Exception as e:
        print("Ошибка при расчете общей пропускной способности:", e)

if __name__ == "__main__":
    test_network_switch()

# Класс №3 "Firewall"

from task_1 import Firewall

def test_firewall():
    # Проверка корректного создания объекта Firewall
    try:
        fw = Firewall(5)
        print("Firewall успешно создан:", fw.num_rules, fw.filtering_state)
    except Exception as e:
        print("Ошибка при создании Firewall:", e)

    # Проверка некорректного количества правил
    try:
        fw = Firewall(0)
    except ValueError as e:
        print("Установим недопустимое количество правил:", e)

    # Проверка метода toggle_filtering
    try:
        fw = Firewall(3)
        fw.toggle_filtering(True)
        print("Состояние фильтрации включено:", fw.filtering_state)
        fw.toggle_filtering(False)
        print("Состояние фильтрации отключено:", fw.filtering_state)
    except Exception as e:
        print("Ошибка при переключении фильтрации:", e)

    # Проверка метода add_rule
    try:
        fw = Firewall(2, True)
        print(fw.add_rule("Allow TCP 80"))
        print(fw.add_rule("Deny UDP 53"))
        print("Список правил:", fw.list_rules())
        fw.add_rule("Block ICMP")
    except ValueError as e:
        print("Переполнение списка правил:", e)

    # Проверка добавления правила при отключенной фильтрации
    try:
        fw.toggle_filtering(False)
        fw.add_rule("Allow ICMP")
    except ValueError as e:
        print("Добавление правил при отключенной фильтрации:", e)

if __name__ == "__main__":
    test_firewall()

