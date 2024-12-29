class NetworkDevice:
    """
    Базовый класс для сетевых устройств.

    Атрибуты:
        name (str): Имя устройства.
        ip_address (str): IP-адрес устройства.
        mac_address (str): MAC-адрес устройства.
    """

    def __init__(self, name: str, ip_address: str, mac_address: str):
        self.name = name
        self.ip_address = ip_address
        self._mac_address = mac_address  # Защищённый атрибут, так как MAC-адрес не должен изменяться извне.

    def __str__(self) -> str:
        return f"NetworkDevice(name={self.name}, ip_address={self.ip_address})"

    def __repr__(self) -> str:
        return f"<NetworkDevice(name='{self.name}', ip_address='{self.ip_address}', mac_address='{self._mac_address}')>"

    def ping(self, target_ip: str) -> str:
        """
        Метод для отправки ping-запроса к другому устройству.

        Аргументы:
            target_ip (str): Целевой IP-адрес.
        Возвращает:
            str: Результат ping-запроса.
        """
        return f"Pinging {target_ip} from {self.ip_address}... Success"


class Router(NetworkDevice):
    """
    Дочерний класс для маршрутизаторов.

    Атрибуты:
        name (str): Имя устройства.
        ip_address (str): IP-адрес устройства.
        mac_address (str): MAC-адрес устройства.
        routes (list): Список маршрутов.
    """

    def __init__(self, name: str, ip_address: str, mac_address: str, routes=None):
        super().__init__(name, ip_address, mac_address)
        self.routes = routes or []  # Если маршруты не заданы, инициализируем пустым списком.

    def __str__(self) -> str:
        # Расширяем строковое представление для маршрутизаторов, добавляя информацию о маршрутах.
        return f"Router(name={self.name}, ip_address={self.ip_address}, routes={len(self.routes)} routes)"

    def add_route(self, route: str) -> None:
        """
        Метод для добавления нового маршрута.

        Аргументы:
            route (str): Новый маршрут.
        """
        self.routes.append(route)

    def ping(self, target_ip: str) -> str:
        """
        Переопределение метода ping для маршрутизатора.

        Причина переопределения: Маршрутизатор может добавлять маршруты при выполнении ping-запроса.
        """
        if target_ip not in self.routes:
            self.routes.append(target_ip)  # Добавляем маршрут, если он отсутствует.
        return f"Router {self.name} pinging {target_ip}... Success"


# Пример использования классов
if __name__ == "__main__":
    # Создаем сетевое устройство
    device = NetworkDevice(name="Switch", ip_address="192.168.1.2", mac_address="00:1B:44:11:3A:B7")
    print(device)
    print(device.ping("192.168.1.1"))

    # Создаем маршрутизатор
    router = Router(name="MainRouter", ip_address="192.168.1.1", mac_address="00:1A:2B:3C:4D:5E")
    print(router)
    router.add_route("192.168.2.0/24")
    print(router.ping("192.168.3.1"))
    print(router)
