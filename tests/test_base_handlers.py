from bot.handlers.base_handlers import clean


def test_clean():
    src_text = "детали переноса【36:1†CLINICA_INFO.md】."
    res = clean(src_text)
    assert res == "детали переноса."

    src_text = """Доктор Валерий Юрьевич Стайсупов выполняет следующие операции:

1. Ринопластика - только закрытым методом. Это одна из его любимых операций, в которой он специализируется【4:0†DOCTOR_INFO.md】【4:1†CATEGORY_00.md】.
2. Липосакция и липоскульптурирование - включает удаление жировых отложений в различных зонах тела【4:0†DOCTOR_INFO.md】【4:12†CATEGORY_00.md】.
3. Абдоминопластика - классическая и мини-абдоминопластика для коррекции формы живота【4:0†DOCTOR_INFO.md】【4:18†CATEGORY_00.md】.
4. Операции на молочной железе - такие как маммопластика с использованием круглых имплантов【4:0†DOCTOR_INFO.md】【4:10†CATEGORY_00.md】.
5. Омолаживающие операции - включает периорбитопластику и другие виды лифтинга лица【4:0†DOCTOR_INFO.md】【4:7†CATEGORY_00.md】【4:15†CATEGORY_00.md】.

Доктор не проводит операции мужчинам, повторные маммопластики и вторичные ринопластики【4:1†CATEGORY_00.md】【4:5†CLINICA_INFO.md】【4:7†CATEGORY_00.md】."""
    expected_text = """Доктор Валерий Юрьевич Стайсупов выполняет следующие операции:

1. Ринопластика - только закрытым методом. Это одна из его любимых операций, в которой он специализируется.
2. Липосакция и липоскульптурирование - включает удаление жировых отложений в различных зонах тела.
3. Абдоминопластика - классическая и мини-абдоминопластика для коррекции формы живота.
4. Операции на молочной железе - такие как маммопластика с использованием круглых имплантов.
5. Омолаживающие операции - включает периорбитопластику и другие виды лифтинга лица.

Доктор не проводит операции мужчинам, повторные маммопластики и вторичные ринопластики."""
    assert clean(src_text) == expected_text
