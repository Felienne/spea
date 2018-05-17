from pathlib import Path
import json

def get_extension(filename):
    return filename[-4:]

def get_type(filename):
    #split the string (ie.7183 Python Basics/01 Chapter 1.1 - About Printing/01 Printing numbers/77110_01_text.step)
    # on underscores
    underscore_parts = filename.split('_')

    #the last part is the type ie _text.step
    type_part = underscore_parts[-1]

    #now remove the .step part

    return type_part[:-5]

def print_recursive(path_string):
    p = Path(path_string)

    for file_or_folder in p.iterdir():
        if file_or_folder.is_dir():
            f = Path(str(file_or_folder) + '/')
            print_recursive(f)
        else:
            print(file_or_folder)

def get_all_step_files(path, all_files):
    for file_or_folder in path.iterdir():

        if file_or_folder.is_dir():
            #print(str(file_or_folder) + " is a folder")
            get_all_step_files(file_or_folder, all_files)

        if file_or_folder.is_file():
            #print(str(file_or_folder) + " is a file")
            if get_extension(str(file_or_folder)) == 'step':
                all_files.append(file_or_folder)
    return all_files


all_files = get_all_step_files(Path('.'), [])
#print(all_files)

html_text = ''

#step_file = all_files[0]
chapter = ''
lesson = ''
for step_file in all_files:
    step_file_string = str(step_file)
    all_levels = step_file_string.split('/')

    current_chapter = all_levels[1]
    #if we are entering a new chapter, compared to the previous file
    #we print an H2 header
    if current_chapter != chapter:
        html_text += '<h2>{0}</h2>'.format(current_chapter)
        chapter = current_chapter

    current_lesson = all_levels[2]
    # if we are entering a new lesson, compared to the previous file
    # we print am H3 header
    if current_lesson != lesson:
        html_text += '<h3>{0}</h3>'.format(current_lesson)
        lesson = current_lesson

    step = all_levels[3]

    #read the json from the file and parse it
    f = open(step_file)
    contents = f.read()

    json_tree = json.loads(contents)


    type_of_file = get_type(step_file_string)

    if type_of_file == 'text':
        text = json_tree['block']['text']

        print(text)
        html_text += '{0}'.format(text)




    if type_of_file == 'code':
        # in the case of a code block, we want to include 2 things:
        # 1) the text above the block, as is (HTML)
        # 2) the code, encoded in <code> tags
        # there are 2 places where there is code in the JSON file, in code_templates
        # and also source, templates.
        # it seems the former is what the students see and the latter
        # what we inputted

        text = json_tree['block']['text']
        code = json_tree['block']['options']['code_templates']['python3']

        print(text)
        html_text += '<br>{0}</br>'.format(text)

        # what we also want to do, it to save the python as a file
        # that way, people can execute the programs offline

        # we create a path to store the file
        path = 'Python files/' + chapter + '/' + lesson + '/' + step + '.py'

        # and print the path to the HTML too
        html_text += '<p>Code below is found in {}</p>'.format(path)
        html_text += '<hr><p><code>{0}</code></p><hr>'.format(code)


        Python_file = open(path, 'w')

        # we will the file with the assignment (text)
        text = text.replace('<b>', '')
        text = text.replace('</b>', '')
        text = text.replace('<p>', '\n')
        text = text.replace('</p>', '\n')
        text = text.replace('<br>', '\n')
        text = text.replace('</br>', '\n')



        Python_file.write('# {0}'.format(text))

        #and the code so it can be executed
        Python_file.write('\n' + code)
        Python_file.close()

html_file = open('output.html', 'w')
html_file.write(html_text)
html_file.close()
