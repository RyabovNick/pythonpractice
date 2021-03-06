import random
import sys

def process_line(line):
    '''
    Извлечение пары (слово, новое_слово).

    Example:
    process_line("Мороз и солнце, день чудесный!") =
    {'BEGIN': ['Мороз'], 
    'Мороз': ['и'], 
    'и': ['солнце,'], 
    'солнце,': ['день'], 
    'день': ['чудесный!'], 
    'чудесный!': ['END']}
    
    В примере добавляется BEGIN и END, чтобы понять когда начинается
    и заканчивается предложение.
    '''
	
	# Ваш код #
	
	pass
	
def process_textfile(filename):
    '''
    Создайте словарь с парами переходов

    Для начала используйте текст (f). Потом он будет
    изменён на I/O.

    Словарь должен содержать следующие пары ключ-значение.
    На примере текста (f).

    'Вся,': ['комната']
    'И': ['ты', 'ель', 'речка', 'навестим', 'берег,']
    'в': ['окно:', 'санки']
    '''
    d = {}

    # Текст до того момента, пока не будет добавлен I/O
    f = '''Мороз и солнце, день чудесный!
	Еще ты дремлешь, друг прелестный –
	Пора, красавица, проснись;
	Открой сомкнуты негой взоры
	Навстречу северной Авроры,
	Звездою севера явись!
	Вечор, ты помнишь, вьюга злилась,
	На мутном небе мгла носилась;
	Луна, как бледное пятно,
	Сквозь тучи мрачные желтела,
	И ты печальная сидела –
	А нынче... погляди в окно:
	Под голубыми небесами
	Великолепными коврами,
	Блестя на солнце, снег лежит;
	Прозрачный лес один чернеет,
	И ель сквозь иней зеленеет,
	И речка подо льдом блестит.
	Вся комната янтарным блеском
	Озарена. Веселым треском
	Трещит затопленная печь.
	Приятно думать у лежанки.
	Но знаешь: не велеть ли в санки
	Кобылку бурую запречь?
	Скользя по утреннему снегу,
	Друг милый, предадимся бегу
	Нетерпеливого коня
	И навестим поля пустые,
	Леса, недавно столь густые,
	И берег, милый для меня.
	'''

	# Ваш код #
	
	pass
	
def generate_line(d):
    '''
	Генерируем рандомные предложения на основе
	созданного словаря с парами 
	
	Заметьте, что первое состояние BEGIN,
	но возвращать это не нужно
    '''

    # Ваш код #

    pass
	
if __name__ == '__main__':
    #if len(sys.argv) != 2:
    #    print('ERROR: Run as python markov.py <filename>')
    #    exit()
    process_textfile('t')
    #process_line("Мороз и солнце, день чудесный!")
    
    #d = process_textfile(sys.argv[1])
    #print(generate_line(d))