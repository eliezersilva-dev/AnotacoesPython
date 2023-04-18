"""
import re - importar o Regex
padrao = re.compile(r'padrao') - cria um padrao para consulta
padrao = re.compile(r'padrao') - o 'r' indica uma expressão Regex
 

Metacaracteres:
. -corresponde a um único caractere de qualquer caractere único, exceto o final de uma linha. Exemplo, o regex abaixo corresponde a camisa, short e qualquer caractere entre sh e rt.
-> sh.rt

^ -corresponde a um termo se o termo aparecer no início de um parágrafo ou linha. Exemplo, o regex abaixo corresponde a um parágrafo ou uma linha que começa com Apple.
-> ^Apple

[^] -dentro de um colchete. Exemplo, o regex abaixo corresponde a qualquer caractere, exceto a, b, c, d, e.
-> [^a-e]

$ -corresponde a um termo se o termo aparecer no final de um parágrafo ou linha. Exemplo, o regex abaixo corresponde a um parágrafo ou uma linha que termina com bye.
-> bye$

[ ] -corresponde a qualquer caractere único da lista entre colchetes. Exemplo, o regex abaixo corresponde a bad, bed, bcd, brd e bod.
-> b[aecro]d

– Hífen -usado para representar um intervalo de letras ou números, geralmente usado dentro de um colchete. Exemplo, o regex abaixo corresponde a kam, kbm, kcm, k2m, k3m, k4m e k5m.
-> k[a-c2-5]m

( ) -agrupa uma ou mais expressões regulares. Exemplo, o regex abaixo corresponde a site.com, site.net e site.org.
-> site\.(com|net|org)

{n} -colchetes com 1 número dentro, corresponde exatamente n vezes ao caractere anterior. Exemplo, a expressão regular abaixo corresponde à string de 4 dígitos e apenas à string de quatro dígitos porque há ^ no início e $ no final da regex.
-> ^[\d]{4}$

{n,m} -colchetes com 2 números dentro, corresponde ao número mínimo e máximo de vezes do caractere anterior. Exemplo, a expressão regular abaixo corresponde a google, gooogle e gooogle.
-> go{2,4}gle

{n,} -colchetes com um número e uma vírgula, corresponde ao número mínimo de vezes o caractere anterior. Exemplo, o regex abaixo corresponde a google, gooogle, gooooogle, gooooooogle, ….
-> go{2,}gle

| -corresponde à expressão regular que a precede ou à expressão regular que a segue (equivale a 'ou'). Exemplo, o regex abaixo corresponde ao formato de data MM/DD/AAAA, MM.DD.AAAA e MM-DD-AAAA. Também corresponde a MM.DD-AAAA, etc.
-> ^(0[1-9]|1[012])[-/.](0[1-9]|[12][0-9]|3[01])[-/.][0-9]{4}$

? -corresponde a 1 ou 0 caractere na frente do ponto de interrogação. Exemplo, a expressão regular abaixo corresponde a apple e apples.
-> apples?

* -corresponde a 0 ou mais caracteres na frente do asterisco. Exemplo, a expressão regular abaixo corresponde a cl,col,cool,cool,…,coooooooooool,…
-> co*l

+ -corresponde a 1 ou mais caracteres na frente do sinal de mais. Exemplo, a expressão regular abaixo corresponde a col,cool,…,coooooooooooool,…
-> co+l

! -não corresponde ao próximo caractere ou expressão regular (negação). Exemplo, a expressão regular abaixo corresponde ao 'q' caractere se o caractere 'q' após não for um dígito, ele corresponderá ao 'q' nas strings de abdqk, quit, qeig, mas não q2kd, sdkq8d.
-> q(?![0-9])

\ -desativa o significado especial do próximo caractere. Exemplo, o regex abaixo trata o ponto como um caractere normal e corresponde apenas a ab.
-> a\.b

\b -Barra invertida e 'b', corresponde a um limite de palavra. Por exemplo, “\bwater” encontra “watergun” mas       não “cleanwater” enquanto “water\b” encontra “cleanwater” mas não “watergun”.
\n -Barra invertida e 'n', representa uma quebra de linha.
\t -Barra invertida e 't', representa uma tabulação.
\w -Barra invertida e 'w', é equivalente a [a-zA-Z0-9_], corresponde a caractere alfanumérico ou sublinhado.        Por outro lado, Maiúscula \W corresponderá a caracteres não alfanuméricos e não a sublinhado.
\d -Barra invertida ed, corresponde aos dígitos de 0 a 9, equivalente a [0-9] ou [:digit]
    [:alpha:] ou [A-Za-z] representa um caractere alfabético.
    [:dígito:] ou [0-9] ou [\d]representa um dígito.
    [:alnum:] ou [A-Za-z0-9] representa um caractere alfanumérico.
\d -procura dígitos
\s -procura por espaços em branco
\w -procura por caracteres de palavras
\A -apenas o início da string
\Z -apenas ao final da string.

Exemplos:

Este regex corresponde aos endereços de e-mail
-> \b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4}\b

Este regex corresponde a links de sites que terminam com sites de .com, .org, .edu, .gov e .br
-> https?://(www\.)?[A-Za-z0-9]+\.(com|org|edu|gov|br)/?.*

Regex corresponde aos números do CPF:
([0-9]{2}[\.]?[0-9]{3}[\.]?[0-9]{3}[\/]?[0-9]{4}[-]?[0-9]{2})|([0-9]{3}[\.]?[0-9]{3}[\.]?[0-9]{3}[-]?[0-9]{2})

Explicação CPF:
[0-9]{2} Faixa de caracteres: 0 a 9, quantidade: 2 caracteres;
[0-9]{3} Faixa de caracteres: 0 a 9, quantidade: 3 caracteres;
[0-9]{4} Faixa de caracteres: 0 a 9, quantidade: 4 caracteres;
[\.]?Um ponto, opcional. Foi usado \ no ponto, pois ele sozinho é caractere especial;
[-]? Um traço, opcional (se acrescentar outros caracteres, comece pelo - sempre);
[\/]? Uma barra, opcional. Tambem "escapada" com \ pra agradar o PCRE;
(grupo1)|(grupo2) Se um dos grupos validar, a expressão é válida.

Caso queira aceitar outros separadores, basta acrescentar entre os [ ].
Exemplo: [-\.\/]? vai aceitar tanto - quanto . e / naquela posição (? = ou nada).

Para adaptar para outros contextos de regexp, algumas variações possíveis seriam tirar o escape da barra (\/ => /) e opcionalmente colocar um ^ no começo e um $ no fim da linha.

Nota: propositalmente usamos [0-9] em vez de \d para que não sejam aceitos outros sets considerados dígitos (como ¹²³ e outras "surpresas" que, por exemplo, o Unicode pode trazer no futuro).


Métodos para checagem:
texto = 'string'
padrao = re.compile(r'padrao')
var = padrao.findall(texto) - retorna todas as observações do padrão
var = padrao.match(texto) - retorna local da str/lista onde se deu o match
var = padrao.serch(texto) - retorna local da str/lista onde se deu a procura
var = padrao.finderinter(texto) - retorna iteradores (pode-se usar o for)


Estruturas:
padrao = re.compile(r'[a-z]') - retorna letras minúsculas
padrao = re.compile(r'[A-Z]') - retorna letras maiúsculas
padrao = re.compile(r'[0-9]') - retorna letras números
padrao = re.compile(r'[a-zA-Z0-9]') - estrutura letras e números
    exemplo de estrutura:
    padrao = re.compile(r'[a-zA-Z] [0-9]') - retorna um padrão de três carcteres
    uma letra 'a-zA-Z', um espaço e um número


Grupos()
expressão dentro de parentêses ()
    exemplo - padrao = re.compile(r'(A|a)?[a-z]{4} [0-9]+')
    pode-se usar o método 'group' para acessar o grupo  
    exemplo - print(padrao.group(1))
    
Exemplo Regex para buscar URLs:
padrao = re.compile(r'https?://(www\.)?([a-zA-Z0-9]+\.)+(com.br|gov.br|com)')

Referências: https://docs.python.org/pt-br/3.8/howto/regex.html
             https://www3.ntu.edu.sg/home/ehchua/programming/howto/Regexe.html
"""
import re

# Exercício - Pegar uma lista de palavras .txt e formatar deixando apenas as palavras (sem pontos ou números);

with open('words.txt', 'r', encoding='utf8') as arquivo:
    palavras = str(arquivo.read())
    print(palavras)

    print()

padrao = re.compile(r'[(a-zA-Z)]+')
formatado = padrao.findall(palavras)
for i in formatado:
    print(i)






