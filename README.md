# SIMulador de Pipeline e Assembly
- Disponível em: https://simpa-hss6.onrender.com
- Disciplina: SSC0902 - Organização e Arquitetura de Computadores
- Para entender o conteúdo no qual se baseia, leia 'Notas de Aula.pdf'
![image](https://github.com/user-attachments/assets/82ca127b-067d-4caf-a4cb-f4e4c9bf3977)


## Objetivos
- Auxiliar o aprendizado de conceitos de programação em baixo nível
- Mostrar o funcionamento de alguns dos tópicos estudados na disciplina
  - Pipeline e registradores intermediários
  - Arquitetura load-store
  - Forwarding e Hazards

## Limitações
- Devido ao escopo do projeto, alguns conceitos foram simplificados
  - A memória, apesar de endereçada a byte, não permite acesso aos bytes individuais
  - Strings são guardadas como se sempre ocupassem 1 palavra
  - Não foram implementadas instruções que precisariam de tratamento de dependências de controle (como jumps e branches)
  - Como a implementação não foi feita em hardware, não houve necessidade de respeitar os formatos de instrução
- Para fins didáticos, um conjunto mínimo de instruções foi implementado
  - ```s
    asciz nome "string"
    word nome valor

    la rd nome
    lw rd imm(rs1)
    sw rs2 imm(rs1)

    add rd rs1 rs2
    addi rd rs1 imm

    pint rs1
    pstr rs1
    ```

## Instruções de Instalação
- Caso prefira uma instalação local, ou a hospedagem do site não esteja mais ativa, os seguintes comandos podem ser utilizados
  - ```
    # Testado com Python 3.12.4
    git clone 'https://github.com/furtadojean/SIMPA.git'
    cd SIMPA
    pip install -r requirements.txt
    uvicorn main:app --host 0.0.0.0 --port 8080
    ```

## Estrutura
- Em lib, encontram-se os códigos para os blocos básicos do sistema, como a definição de um componente e os tipos de dado que possuem, além do parser, memória etc
- Em template, encontram-se os componentes do caminho de dados, que usam das classes definidas em lib
- Em templates, encontram-se os templates html do Jinja2
- Sobre a stack utilizada
  - FastAPI para o backend, utilizando Jinja2 para auxiliar a retornar páginas html
  - HTMX e Tailwind no frontend
  - CodeMirror para o editor de código no browser
