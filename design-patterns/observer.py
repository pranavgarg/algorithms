
class WeatherData implements Subject:
    def __init__(self):
        self.observers = []
        self.temperature = None
        self.humidity = None
        self.pressure = None

    def registerObserver(self, o):
        self.observers.add(o)

    def removeObserver(self, o):
        self.observers.remove(o)

    def notifyObservers(self):
        #send message to observers
        pass

    def measurementsChanged(self):
        self.notifyObservers()

    def setMeasureements(self, temperature, pressure, humidity):
        self.