import doctest

# Класс №1 "IP_packet"

class IP_packet:
    def __init__(self, packet_size: int, ttl: int):
        """
        Создание IP пакета"

        :param packet_size: Размер пакета в байтах
        :param ttl: Время жизни пакета (Time To Live)

        Примеры:
        >>> packet = IP_packet(1400, 64)
        >>> packet.packet_size
        1400
        >>> packet.ttl
        64
        """
        if not isinstance(packet_size, int) or not isinstance(ttl, int):
            raise TypeError("Размер пакета и TTL должны быть целыми числами")

        if packet_size > 1500:
            raise ValueError("Размер пакета не может превышать 1500 байт")
        self.packet_size = packet_size

        if ttl <= 1:
            raise ValueError("TTL должен быть больше 1")
        self.ttl = ttl

    def forward_packet(self) -> str:
        """
        Пересылка пакета если TTL больше 1, иначе уничтожение пакета.

        :return: Сообщение о пересылке или уничтожении пакета

        Примеры:
        >>> packet = IP_packet(1400, 64)
        >>> packet.forward_packet()
        'Пакет пересылается.'
        """
        if self.ttl > 1:
            return "Пакет пересылается."
        else:
            return "Пакет уничтожен из-за TTL = 1"

    def decrease_ttl(self, decrease_by: int = 1) -> None:
        """
        Уменьшение значения TTL на заданное количество.

        :param decrease_by: Сколько уменьшить TTL (по умолчанию 1)
        :raise ValueError: Если TTL становится меньше 1

        Примеры:
        >>> packet = IP_packet(1400, 5)
        >>> packet.decrease_ttl(1)
        >>> packet.ttl
        4
        """
        if not isinstance(decrease_by, int):
            raise TypeError("Количество уменьшения TTL должно быть целым числом")

        if decrease_by < 0:
            raise ValueError("Количество уменьшения не может быть отрицательным")

        self.ttl -= decrease_by

        if self.ttl < 1:
            raise ValueError("TTL не может быть меньше 1")


if __name__ == "__main__":
    doctest.testmod()

# Класс №2 "Switch"

class NetworkSwitch:
    def __init__(self, port_count: int, port_speed: int):
        """
        Создание объекта "Сетевой коммутатор".

        :param port_count: Количество портов (1-48, кратно 2)
        :param port_speed: Скорость порта (100, 1000, 10000 Мбит/с)
        :raise ValueError: Если количество портов или скорость порта невалидны

        Примеры:
        >>> switch = NetworkSwitch(24, 1000)
        >>> switch.port_count
        24
        >>> switch.port_speed
        1000
        """
        if not isinstance(port_count, int) or not (1 <= port_count <= 48):
            raise ValueError("Некорректное количество портов. Допустимо от 1 до 48.")

        if port_count % 2 != 0:
            raise ValueError("Количество портов должно быть кратно двум.")
        self.port_count = port_count

        if port_speed not in [100, 1000, 10000]:
            raise ValueError("Недопустимая скорость порта. Допустимо: 100, 1000, 10000 Мбит/с.")
        self.port_speed = port_speed

        self.ports_status = [True] * port_count  # Все порты активны по умолчанию

    def check_ports_status(self) -> list[bool]:
        """
        Проверяет состояние всех портов.

        :return: Список статусов портов (True - активен, False - неактивен)

        Примеры:
        >>> switch = NetworkSwitch(8, 1000)
        >>> switch.check_ports_status()
        [True, True, True, True, True, True, True, True]
        """
        return self.ports_status

    def update_port_speed(self, new_speed: int) -> None:
        """
        Обновляет скорость всех портов.

        :param new_speed: Новая скорость порта (100, 1000, 10000 Мбит/с)
        :raise ValueError: Если новая скорость порта недопустима

        Примеры:
        >>> switch = NetworkSwitch(16, 100)
        >>> switch.update_port_speed(1000)
        >>> switch.port_speed
        1000
        """
        if new_speed not in [100, 1000, 10000]:
            raise ValueError("Недопустимая скорость порта. Допустимо: 100, 1000, 10000 Мбит/с.")
        self.port_speed = new_speed

    def calculate_total_bandwidth(self) -> int:
        """
        Рассчитывает общую пропускную способность всех активных портов.

        :return: Общая пропускная способность (Мбит/с)

        Примеры:
        >>> switch = NetworkSwitch(12, 1000)
        >>> switch.calculate_total_bandwidth()
        12000
        """
        active_ports = sum(self.ports_status)
        return active_ports * self.port_speed


if __name__ == "__main__":
    doctest.testmod()

# Класс №3 "Firewall"

class Firewall:
    def __init__(self, num_rules: int, filtering_state: bool = False):
        """
        Создание объекта "Firewall".

        :param num_rules: Количество правил (целое число, больше 0)
        :param filtering_state: Состояние фильтрации (включено/выключено)
        :raise ValueError: Если количество правил не больше 0

        Примеры:
        >>> fw = Firewall(5)
        >>> fw.num_rules
        5
        >>> fw.filtering_state
        False
        """
        if not isinstance(num_rules, int) or num_rules <= 0:
            raise ValueError("Количество правил должно быть целым числом больше 0.")
        self.num_rules = num_rules

        self.filtering_state = filtering_state
        self.rules = []

    def add_rule(self, rule: str) -> str:
        """
        Добавляет правило, если фильтрация включена.

        :param rule: Строка, описывающая правило
        :raise ValueError: Если правило не является строкой или фильтрация отключена
        :return: Сообщение о результате

        Примеры:
        >>> fw = Firewall(3, True)
        >>> fw.add_rule("Allow TCP 80")
        'Правило добавлено: Allow TCP 80'
        >>> fw.list_rules()
        ['Allow TCP 80']
        """
        if not self.filtering_state:
            raise ValueError("Невозможно добавить правило: фильтрация отключена.")
        if not isinstance(rule, str):
            raise ValueError("Правило должно быть строкой.")

        if len(self.rules) >= self.num_rules:
            raise ValueError("Достигнуто максимальное количество правил.")

        self.rules.append(rule)
        return f"Правило добавлено: {rule}"

    def toggle_filtering(self, state: bool) -> None:
        """
        Включает или выключает фильтрацию.

        :param state: Состояние фильтрации (True или False)

        Примеры:
        >>> fw = Firewall(3)
        >>> fw.toggle_filtering(True)
        >>> fw.filtering_state
        True
        """
        self.filtering_state = state

    def list_rules(self) -> list[str]:
        """
        Возвращает список всех добавленных правил.

        :return: Список правил

        Примеры:
        >>> fw = Firewall(3, True)
        >>> fw.add_rule("Allow ICMP")
        'Правило добавлено: Allow ICMP'
        >>> fw.list_rules()
        ['Allow ICMP']
        """
        return self.rules


if __name__ == "__main__":
    doctest.testmod()

