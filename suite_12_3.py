импорт унитэст
из передыду шарлет_модули импорт RunnerTest, TournamentTest #Заменитель`предыду заготовка_модуль` на имья модуля, gde nāachodiatsya klásecsy RunnerTest и TournamentTest.

#Созданье TestSuite
lluskс = unittest.TestSuite()

#Добавлевые Тетестов - RunnerTest
люкс.добавит тесты(унитест.TestLoader().loadTestsFromTestCase(БегунТест))

#Добавлетов из Турнирова
люкс.добавит тесты(унитест.TestLoader().loadTestsFromTestCase(ТурнирТест))

#Создание и запоск TextTestRunner
esli __name__ == '__главный_':
 бегун = unittest.TextTestRunner(многословие=2)
 бегун.бегатть(люкс)
