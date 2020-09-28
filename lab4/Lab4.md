### Лабораторушка 4

#### Задание

Вам дан `paper.tex`. 

Добавьте туда еще простейший граф, вам поможет GraphViz (`dot -Tpng -o <имя-выходного-файла.png> <входной-файл.gv>`).

А еще, можно поиграться с `matplotlib` и добавить разные [графики](https://benalexkeen.com/bar-charts-in-matplotlib/).

Сравните возможнности [plantuml](https://plantuml.com/) и [mermaid](https://mermaid-js.github.io/mermaid/).

Добавьте в свой документ что-то что умеет только `mermaid` (например pie charts) и что-то, что умеет только `plantUML`.

Вызывать их можно так:
- `puml -charset utf-8 -tpng -I gantt.puml`
- `mmdc -i gantt.mmd -o gantt.png`

```
$ cat $(which puml)
java -jar /Users/ravil/apps/plantuml.jar $@
```

#### Задание 
Вам дан следующий `students.xml`

```xml
<students>
    <student>
        <name>Iwan Petrow</name>
        <year>2018</year>
        <note>otlicznik</note>
        <courses>
            <course id="course_1"><name>Алгоритмы</name></course>
        </courses>
    </student>
    <student>
        <name>Petr Ivanow</name>
        <year>2018</year>
        <courses>
            <course id="course_1"><name>Алгоритмы</name></course>
            <course id="course_2"><name>Базы данных</name></course>
            <course id="course_3"><name>Практический минимум</name></course>
            <course id="course_4"><name>С++</name></course>
        </courses>
    </student>
</students>
```

Напишите xpath-выражение которое найдет имена студентов, записанных на более чем один курс.

```
xmlstarlet sel -t -v <Ваш xpath> students.xml
```

Вам может помочь [w3schools](https://www.w3schools.com/xml/default.asp).

#### Задание 
Вам дан следующий `students.xquery`

```xml
let $doc :=
<csc>
    <courses>
        <course id="course_1"><name>Алгоритмы</name></course>
        <course id="course_2"><name>Базы данных</name></course>
        <course id="course_3"><name>Практический минимум</name></course>
        <course id="course_4"><name>С++</name></course>
    </courses>
    <students>
        <student>
            <name>Super Student</name>
            <year>2018</year>
            <note>otlicznik</note>
            <study courses="course_1 course_2" />
        </student>
        <student>
            <name>Drugoi Student</name>
            <year>2018</year>
            <study courses="course_2 course_3" />
        </student>
    </students>
</csc>
```

Напишите xquery, который покажет какой студент записан на какой курс.

Пример ответа
```shell script
$ xqilla students.xquery
<result student="Super Student" course="Алгоритмы"/>
<result student="Super Student" course="Базы данных"/>
<result student="Drugoi Student" course="Базы данных"/>
<result student="Drugoi Student" course="Практический минимум"/>
```

Вам может помочь [w3schools](https://www.w3schools.com/xml/default.asp).

#### Задание 

Напишите `XSD` схему для какого либо из документов выше. 
Есть онлайн-ресурсы, которые могут помочь вам построить `XSD` по заданному `XML` и останется чуть-чуть доработать напильником.

#### Задание 

Опишите любой из файлов выше в [ProtoBuf](https://developers.google.com/protocol-buffers).

Возможно вам поможет [онлайн protobuf компилятор](http://protobuf-compiler.herokuapp.com/)
или [json-to-protobuf](https://www.site24x7.com/tools/json-to-protobuf.html).
