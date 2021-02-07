"""
  Módulo Collection - Counter

  Collections -> High-Performance Container Datatypes

  Counter -> Recebe um iterável como parâmetro e cria um objeto do tipo Collection Counter que é parecido com um
  dicionáriom contendo como chave o elemento da lista passada como parâmetro e como valor a quantidade

"""
# Importaro Counter

from collections import Counter

# Exemplo 1
"""lista = [1, 1, 1, 2, 2, 3, 3, 3, 3, 1, 1, 1, 5, 5, 5, 4, 4,4 , 45, 5, 45, 6, 7, 6, 5, 6, 6, 5, 4, 3, 44, 555, 33, 2]

res = Counter(lista)
print(res)
print(type(res))"""

# Counter({1: 6, 5: 6, 3: 5, 4: 4, 6: 4, 2: 3, 45: 2, 7: 1, 44: 1, 555: 1, 33: 1})
# Para cada elemento da lista o Counter criou uma CHAVE e como 'VALOR' ele informa
#   a quantidade de ocorrencias daquela 'CHAVE'

# Exemplo 2
print(Counter('Andrews Schulla Fernandes'))
# Counter({'n': 3, 'e': 3, 'd': 2, 'r': 2, 's': 2, ' ': 2, 'l': 2, 'a': 2, 'A': 1, 'w': 1, 'S': 1, 'c': 1, 'h': 1,
# 'u': 1, 'F': 1})

# Exemplo 3
texto = """A implantação, na prática, prova que o consenso sobre a utilização da orientação a objeto afeta 
positivamente o correto provisionamento da utilização dos serviços nas nuvens. O que temos que ter sempre em mente é 
que a lei de Moore causa uma diminuição do throughput da confidencialidade imposta pelo sistema de senhas. Por outro 
lado, a disponibilização de ambientes assume importantes níveis de uptime do fluxo de informações. A certificação de 
metodologias que nos auxiliam a lidar com a determinação clara de objetivos pode nos levar a considerar a 
reestruturação da gestão de risco. 

          Assim mesmo, a consolidação das infraestruturas inviabiliza a implantação de alternativas aos aplicativos 
          convencionais. Considerando que temos bons administradores de rede, o desenvolvimento de novas tecnologias 
          de virtualização representa uma abertura para a melhoria do impacto de uma parada total. Do mesmo modo, 
          a consulta aos diversos sistemas cumpre um papel essencial na implantação do tempo de down-time que deve 
          ser mínimo. 

          Neste sentido, o novo modelo computacional aqui preconizado estende a funcionalidade da aplicação dos 
          procedimentos normalmente adotados. Pensando mais a longo prazo, o crescente aumento da densidade de bytes 
          das mídias talvez venha causar instabilidade das ACLs de segurança impostas pelo firewall. Nunca é demais 
          lembrar o impacto destas possíveis vulnerabilidades, uma vez que a utilização de recursos de hardware 
          dedicados otimiza o uso dos processadores dos equipamentos pré-especificados. 

          O cuidado em identificar pontos críticos no uso de servidores em datacenter imponha um obstáculo ao upgrade 
          para novas versões dos paradigmas de desenvolvimento de software. As experiências acumuladas demonstram que 
          a revolução que trouxe o software livre exige o upgrade e a atualização das ferramentas OpenSource. 
          Todavia, a constante divulgação das informações implica na melhor utilização dos links de dados da garantia 
          da disponibilidade. O empenho em analisar a necessidade de cumprimento dos SLAs previamente acordados 
          apresenta tendências no sentido de aprovar a nova topologia das janelas de tempo disponíveis. No mundo 
          atual, o aumento significativo da velocidade dos links de Internet acarreta um processo de reformulação e 
          modernização do sistema de monitoramento corporativo. 

          Evidentemente, o desenvolvimento contínuo de distintas formas de codificação facilita a criação das novas 
          tendencias em TI. No entanto, não podemos esquecer que o índice de utilização do sistema oferece uma 
          interessante oportunidade para verificação dos índices pretendidos. Acima de tudo, é fundamental ressaltar 
          que a alta necessidade de integridade é um ativo de TI dos métodos utilizados para localização e correção 
          dos erros. Não obstante, a implementação do código faz parte de um processo de gerenciamento de memória 
          avançado das direções preferenciais na escolha de algorítimos. 

          O incentivo ao avanço tecnológico, assim como o entendimento dos fluxos de processamento deve passar por 
          alterações no escopo das formas de ação. """

palavras = texto.split()
# print(palavras)
res = Counter(texto)
print(res)
res = Counter(palavras)
print(res)

# Most_Common - Traz nesse caso as 5 palavras de maior ocorrência no texto.
print(res.most_common(5))
