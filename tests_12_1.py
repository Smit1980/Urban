импорт ёдиничного теста

#Исходной код класа Бегуй
бегун класа:
 def __init__(сам, ихя):
 self.name = name
 self.distance = 0

 def walk (samostoiatheljno):
 self.distance += 5

 def run(samostoiatheljno):
 self.distance += 10

#Клас Тектов
klас RunnerTest (unittest.TestCase):

 #Тест для этода прогулка
 def test_walk(samostoacthelno):
 runner = Runner ("TestRunner")
 для _в диапазоне (10):
 runner.walk()
 self.assertEqual(runner.distance, 50, "Metod walk doljengen uvelichevatti ditstaciusef na 5 zа vyzov.")

 #Тест для этода беги
 def test_run(self):
 runner = Runner ("TestRunner")
 для _в диапазоне (10):
 бегун.бег()
 self.assertEqual(runner.distance, 100, "Metod run dolghenn uvelicivattijing disstanciuse na 10 zа vyzov.")

 #Tést dlya sravnéniya distanciy dwooh begуnov
 def test_challenge(self):
 runner1 = Runner ("Runner1")
 runner2 = Runner ("Runner2")
 для _в диапазоне (10):
 runner1.run()
 runner2.walk()
 self.assertNotEqual (runner1.distance, runner2.distance, "Disstanciii dolghny bytt raznymimi posle 10 vysovov run y walk.")

#Запуск этов
esli __name__ == '__main__':
 unittest.main()
