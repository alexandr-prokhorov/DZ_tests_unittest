import unittest

from task_1 import Teacher, DisciplineTeacher


class TestTeacher(unittest.TestCase):
    def setUp(self):
        """
        Функция инициализирует объекты классов для тестов
        """
        self.teacher1 = Teacher(name="Иван Иванов", education="БГПУ", experience=4)
        self.teacher2 = DisciplineTeacher(name="Сергей Сергеев", education="МГУ", experience=6,
                                          discipline="Информатика", job_title="Преподаватель")

    def test_teacher_initialization(self):
        """
        Функция тестирует инициализации объекта Teacher.
        """
        self.assertEqual(self.teacher1.name, "Иван Иванов")
        self.assertEqual(self.teacher1.education, "БГПУ")
        self.assertEqual(self.teacher1.experience, 4)

    def test_discipline_teacher_initialization(self):
        """
        Функция тестирует инициализации объекта DisciplineTeacher.
        """
        self.assertEqual(self.teacher2.name, "Сергей Сергеев")
        self.assertEqual(self.teacher2.education, "МГУ")
        self.assertEqual(self.teacher2.experience, 6)
        self.assertEqual(self.teacher2.discipline, "Информатика")
        self.assertEqual(self.teacher2.job_title, "Преподаватель")

    def test_experience_setter(self):
        """
        Функция тестирует значение опыта работы.
        """
        self.teacher1.experience = 5
        self.assertEqual(self.teacher1.experience, 5)
        with self.assertRaises(ValueError):
            self.teacher1.experience = -1

    def test_get_teacher_data(self):
        """
        Функция тестирует метода get_teacher_data вывод информации об учителе.
        """
        teacher_data = self.teacher1.get_teacher_data()
        self.assertIn("Иван Иванов", teacher_data)
        self.assertIn("БГПУ", teacher_data)
        self.assertIn("4", teacher_data)

        discipline_teacher_data = self.teacher2.get_teacher_data()
        self.assertIn("Сергей Сергеев", discipline_teacher_data)
        self.assertIn("Информатика", discipline_teacher_data)
        self.assertIn("Преподаватель", discipline_teacher_data)

    def test_add_mark(self):
        """
        Функция тестирует метод add_mark добавление оценки.
        """
        result = self.teacher2.add_mark("Анна", 5)
        self.assertEqual(result,
                         "Преподаватель Сергей Сергеев по предмету Информатика поставил оценку 5 студенту Анна")

    def test_remove_mark(self):
        """
        Функция тестирует метод remove_mark удаление оценки.
        """
        result = self.teacher2.remove_mark("Анна", 4)
        self.assertEqual(result,
                         "Преподаватель Сергей Сергеев по предмету Информатика удалил оценку 4 студенту Анна")

    def test_give_a_consultation(self):
        """
        Функция тестирует метод give_a_consultation о проведенной консультации преподавателем.
        """
        result = self.teacher2.give_a_consultation("10А")
        self.assertEqual(result,
                         "Преподаватель Сергей Сергеев провел консультацию по предмету Информатика в 10А классе")

    def test_dismiss_teacher(self):
        """
        Функция тестирует метода dismiss_teacher удаление учителя или его наличие.
        """
        Teacher.teachers_list = [self.teacher1, self.teacher2]
        result = Teacher.dismiss_teacher("Иван Иванов")
        self.assertEqual(result, "Учитель Иван Иванов уволен.")
        self.assertEqual(len(Teacher.teachers_list), 1)
        self.assertEqual(Teacher.teachers_list[0].name, "Сергей Сергеев")

        result = Teacher.dismiss_teacher("Иван Иванов")
        self.assertEqual(result, "Учитель с именем Иван Иванов не найден.")

    def test_job_title_setter(self):
        """
        Функция проверяет сеттер job_title изменение в должности.
        """
        self.teacher2.job_title = "Директор"
        self.assertEqual(self.teacher2.job_title, "Директор")
