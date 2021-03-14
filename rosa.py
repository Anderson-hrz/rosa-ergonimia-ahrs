import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import pandas as pd


st.set_option('deprecation.showPyplotGlobalUse', False)

st.title("""**ROSA - Rapid Office Strain Assessment**""")
#st.write("""O objetivo desta ferramenta é gerar códigos de gráficos de forma fácil.\n
#Os parâmetros customizáveis nesta ferramenta são os mais usuais, se você desejar customizar ainda mais seus gráficos, consulte a documentação oficial ou tutoriais sobre o Matplotlib.""")

#st.write("""Selecione o tipo de gráfico desejado na barra lateral e as demais opções disponíveis. Assim que o botão Plotar aparecer, clique no mesmo.\n
#Então será criado o código do gráfico e a plotagem do mesmo. Basta copiar o código e usar em seu próprio projeto. Por fim, altere os dados de entrada conforme sua necessidade e demais ajustes se desejável.""")
#st.sidebar.write("""# **Gráficos **""")

st.title("**Seção A**")
st.write("**Altura do assento. **")
image_a = Image.open('A.jpg')
st.image(image_a)


# Altura do assento.
lista_altura_do_assento = []

altura_do_assento = st.selectbox('Selecione uma única opção. Resposta obrigatória.', ["Selecione", "Joelhos à 90° (1)",
	"Muito Baixo - Joelhos< 90° (2)",
	"Muito Alto - Joelhos> 90° (2)",
	"Pés sem contato com o chão(3)"],  key="altura_do_assento")

lista_altura_do_assento.append(altura_do_assento)

adicional_altura_do_assento = st.multiselect('Adicionais altura do assento. Permite múltipla seleção. Reposta somente se necessária.', ["Espaço insuficiente embaixo da mesa (+1)", "Altura não ajustável (+1)"], key="adicional_altura_do_assento")
#st.write(adicional_altura_do_assento)

# Inserindo na mesma lista
try:
	lista_altura_do_assento.extend(adicional_altura_do_assento)
except:
	pass

try:
	lista_altura_do_assento = ";".join(lista_altura_do_assento)
except:
	pass

lista_altura_do_assento_valida  = []
lista_altura_do_assento_valida.append(lista_altura_do_assento)

#st.write(lista_altura_do_assento_valida)
#st.write(type(lista_altura_do_assento_valida))


# Profundidade do assento
st.write("**Profundidade do assento**")
image_b = Image.open('B.jpg')
st.image(image_b)

lista_profundidade_do_assento = []

profundidade_do_assento = st.selectbox('Selecione uma única opção. Resposta obrigatória.', ["Selecione", "Aprox. 7,5 cm entre joelho e final da cadeira (1)",
	"Muito próximo - espaço",
	"Muito distante - espaço >7,5 cm (2)"], key="profundidade_do_assento")

lista_profundidade_do_assento.append(profundidade_do_assento)

adicional_profundidade_do_assento = st.multiselect('Adicional da profundidade do assento. Reposta somente se necessária.', ["Não ajustável (+1)"], key="adicional_profundidade_do_assento")


# Inserindo na mesma lista
try:
	lista_profundidade_do_assento.extend(adicional_profundidade_do_assento)
except:
	pass

try:
	lista_profundidade_do_assento = ";".join(lista_profundidade_do_assento)
except:
	pass

lista_profundidade_do_assento_valida  = []
lista_profundidade_do_assento_valida.append(lista_profundidade_do_assento)
#st.write(lista_profundidade_do_assento_valida)


# Descanso do braço
st.write("**Descanso de braço**")
image_c = Image.open('C.jpg')
st.image(image_c)

lista_descanso_de_braco = []

descanso_de_braco = st.selectbox('Selecione uma única opção. Resposta obrigatória.', ["Selecione", "Suporte doombro alinhado com cotovelo - ombro relaxado (1)",
	"Muito alto (ombros abduzidos)/ Baixo (braço sem suporte) (2)"], key="descanso_de_braco")


lista_descanso_de_braco.append(descanso_de_braco)


adicional_descanso_de_braco = st.multiselect('Adicionais descanso de braço. Permite múltipla seleção. Reposta somente se necessária.', ["Superfície escorregadia ou danificada (+1)","Muito Largo (+1)", "Não ajustável (+1)"], key="adicional_descanso_de_braco")


# Inserindo na mesma lista
try:
	lista_descanso_de_braco.extend(adicional_descanso_de_braco)
except:
	pass

try:
	lista_descanso_de_braco = ";".join(lista_descanso_de_braco)
except:
	pass
#st.write(lista_descanso_de_braco)

# Suporte para as costas
st.write("**Suporte para as costas**")
image_d = Image.open('D.jpg')
st.image(image_d)

lista_suporte_para_as_costas = []

suporte_para_as_costas = st.selectbox('Selecione uma única opção. Resposta obrigatória.', ["Selecione", "Apoio lombar correto - cadeira reclinada entre95-110° (1)",
	"Sem apoio lombar OU suporte não corretamentena parte inferior das costas (2)",
	"Muito para trás(>110°) / Muito para frente (< 95°) (2)",
	"Sem suporte para costas (banco)/ Trabalho de leituras com tronco parafrente (2)"
	], key="suporte_para_as_costas")

lista_suporte_para_as_costas.append(suporte_para_as_costas)

adicional_suporte_para_as_costas = st.multiselect('Adicionais suporte para as costas. Permite múltipla seleção. Reposta somente se necessária.', ["Área de trabalho muito alta (ombros abduzidos)  (+1)", 
	"Apoio lombar sem ajustes (+1)"], key="adicional_suporte_para_as_costas")


# Inserindo na mesma lista
try:
	lista_suporte_para_as_costas.extend(adicional_suporte_para_as_costas)
except:
	pass

try:
	lista_suporte_para_as_costas = ";".join(lista_suporte_para_as_costas)
except:
	pass
#st.write(lista_suporte_para_as_costas)


# Secao A duracao
st.write("**Seção A duração**")

lista_secao_A_duracao = []

secao_A_duracao = st.selectbox('Selecione uma única opção. Resposta obrigatória.', ["Selecione", "> 1 h de forma continua ou mais que 4 h por dia (+1)",
	"Entre 30 min a 1 h de forma continua ou entre 1 e 4 h por dia (0)",
	"< 30 minutos de forma contínua, ou menos do que uma hora por dia (-1)"], key="secao_A_duracao")

lista_secao_A_duracao.append(secao_A_duracao)
#st.write(lista_secao_A_duracao)


# Monitor
st.title("**Seção B**")
st.write("**Monitor**")
image_e = Image.open('E.jpg')
st.image(image_e)

lista_monitor = []

monitor = st.selectbox('Selecione uma única opção. Resposta obrigatória.', ["Selecione", "Distância de um braço (40 - 75 cm) / Monitor na altura dos olhos (1)",
	"Muito perto (< 30°)(2)",
	"Muito Alto - cabeça em extensão(3)"], key="Monitor")

lista_monitor.append(monitor)

adicional_monitor = st.multiselect('Adicionais monitor. Permite múltipla seleção. Reposta somente se necessária.', ["Cabeça rodada maior que 30° (+1)",
	"Brilho na tela (+1)","Sem porta documentos (+1)","Muito longe (+1)"], key="adicional_monitor")

# Inserindo na mesma lista
try:
	lista_monitor.extend(adicional_monitor)
except:
	pass

try:
	lista_monitor = ";".join(lista_monitor)
except:
	pass
#st.write(lista_monitor)



st.write("**Monitor duração**")

lista_monitor_duracao = []

monitor_duracao = st.selectbox('Selecione uma única opção. Resposta obrigatória.', ["Selecione", "> 1 h de forma continua ou mais que 4 h por dia (+1)",
	"Entre 30 min a 1 h de forma continua ou entre 1 e 4 h por dia (0)",
	"< 30 minutos de forma contínua, ou menos do que uma hora por dia (-1)"],  key="monitor_duracao")

# Inserindo na mesma lista
lista_monitor_duracao.append(monitor_duracao)

#st.write(lista_monitor_duracao)


# Telefone
st.write("**Telefone**")
image_f = Image.open('F.jpg')
st.image(image_f)

lista_telefone = []

telefone = st.selectbox('Selecione uma única opção. Resposta obrigatória.', ["Selecione", "Headset /Uma mão no telefone e pescoço em posição neutra (1)",
	"Muito longe para atender (> 30 cm) (2)"], key="monitor_duracao")

lista_telefone.append(telefone)

adicional_telefone = st.multiselect('Adicionais suporte para o telefone. Permite múltipla seleção. Reposta somente se necessária.', ["Segurando com cabeça e ombro (+2)",
	"Sem opção de mãos livres (handset) (+1)"], key="adicional_telefone")

# Inserindo na mesma lista
try:
	lista_telefone.extend(adicional_telefone)
except:
	pass

try:
	lista_telefone = ";".join(lista_telefone)
except:
	pass
#st.write(lista_telefone)


st.write("**Telefone duração**")

lista_telefone_duracao = []

telefone_duracao = st.selectbox('Selecione uma única opção. Resposta obrigatória.', ["Selecione", "> 1 h de forma continua ou mais que 4 h por dia (+1)",
	"Entre 30 min a 1 h de forma continua ou entre 1 e 4 h por dia (0)",
	"< 30 minutos de forma contínua, ou menos do que uma hora por dia (-1)"],  key="telefone_duracao")

lista_telefone_duracao.append(telefone_duracao)
#st.write(lista_telefone_duracao)


#### Mouse
st.title("**Seção C**")
st.write("**Mouse**")
image_g = Image.open('G.jpg')
st.image(image_g)

lista_mouse = []

mouse = st.selectbox('Selecione uma única opção. Resposta obrigatória.', ["Selecione", "Mouse alinhado com o ombro (1)",
	"Mouse afastado / distanteda linha do ombro (2)"], key="mouse")

lista_mouse.append(mouse)

mouse_adicional = st.multiselect('Adicionais mouse. Permite múltipla seleção. Reposta somente se necessária.', ["Mouse e teclado em superfícies diferentes (+2)",
	"Mouse pequeno (mão em garra) (+1)","Apoio de punho em frente ao mouse (+1)"], key="mouse_adicional")

try:
	lista_mouse.extend(mouse_adicional)
except:
	pass

try:
	lista_mouse = ";".join(lista_mouse)
except:
	pass
#st.write(lista_mouse)


st.write("**Mouse duração**")


lista_mouse_duracao = []

mouse_duracao = st.selectbox('Selecione uma única opção. Resposta obrigatória.', ["Selecione", "> 1 h de forma continua ou mais que 4 h por dia (+1)",
	"Entre 30 min a 1 h de forma continua ou entre 1 e 4 h por dia (0)",
	"< 30 minutos de forma contínua, ou menos do que uma hora por dia (-1)"],  key="mouse_duracao")


lista_mouse_duracao.append(mouse_duracao)
#st.write(lista_mouse_duracao)


# Teclado
st.write("**Teclado**")
image_h = Image.open('H.jpg')
st.image(image_h)

lista_teclado = []
teclado = st.selectbox('Selecione uma única opção. Resposta obrigatória.', ["Selecione", "Pulsos neutros /Ombros relaxados (1)",
	"Punhos extendidos  / Teclado com angulo positivo (>15°) (2)"], key="teclado")

lista_teclado.append(teclado)

adicional_teclado = st.multiselect('Adicionais teclado. Permite múltipla seleção. Reposta somente se necessária.', ["Desvio de punho ao digitar(+1)",
	"Teclado alto / ombros abduzidos (+1)", "Pegar coisas acima da cabeça (+1)",
	"Mesa não ajustavél(+1)"], key="adicional_teclado")

try:
	lista_teclado.extend(adicional_teclado)
except:
	pass

try:
	lista_teclado = ";".join(lista_teclado)
except:
	pass
#st.write(lista_teclado)


st.write("**Teclado duração**")

lista_teclado_duracao = []

teclado_duracao = st.selectbox('Selecione uma única opção. Resposta obrigatória.', ["Selecione", "> 1 h de forma continua ou mais que 4 h por dia (+1)",
	"Entre 30 min a 1 h de forma continua ou entre 1 e 4 h por dia (0)",
	"< 30 minutos de forma contínua, ou menos do que uma hora por dia (-1)"],  key="teclado_duracao")

lista_teclado_duracao.append(teclado_duracao)
#st.write(lista_teclado_duracao)



data =  {"Altura do assento: Sec A ROSA - altura do assento":[], 
         "Descanso de braço. Sec A ROSA - descanso de braço":[],
         "Monitor. Sec B ROSA - monitor":[],
         "Mouse. Sec C ROSA - mouse":[],
         "Profundidade do assento. Sec A ROSA - profundidade do assento":[],
         "Seção A duração - ROSA:":[],
         "Seção B monitor duração - ROSA:":[],
         "Seção B telefone duração - ROSA:":[],
         "Seção C mouse duração - ROSA:":[],
         "Seção C teclado duração - ROSA:" :[],
         "Suporte para as costas. Sec A ROSA - suporte para as costas":[],
         "Teclado. Sec C ROSA - teclado":[],
         "Telefone. Sec B ROSA - telefone":[]}

# Validacao
st.write("")
st.write("")
st.write("")

submit = st.button('Analisar')

if submit:	

	if altura_do_assento == "Selecione":
		st.write("**Correção necessária:**")
		st.write("**Selecione uma resposta na Seção A pergunta Altura do assento.**")

	elif profundidade_do_assento == "Selecione":
		st.write("**Correção necessária:**")
		st.write("**Selecione uma resposta na Seção A pergunta Profundidade do assento.**")

	elif descanso_de_braco == "Selecione":
		st.write("**Correção necessária:**")
		st.write("**Selecione uma resposta na Seção A pergunta Descanso do braço.**")

	elif suporte_para_as_costas == "Selecione":
		st.write("**Correção necessária:**")
		st.write("**Selecione uma resposta na Seção A pergunta Suporte para as costas.**")

	elif secao_A_duracao == "Selecione":
		st.write("**Correção necessária:**")
		st.write("**Selecione uma resposta na Seção A pergunta Seção A duração.**")

	elif monitor == "Selecione":
		st.write("**Correção necessária:**")
		st.write("**Selecione uma resposta na Seção B pergunta Monitor.**")

	elif monitor_duracao == "Selecione":
		st.write("**Correção necessária:**")
		st.write("**Selecione uma resposta na Seção B pergunta Monitor duração.**")

	elif telefone == "Selecione":
		st.write("**Correção necessária:**")
		st.write("**Selecione uma resposta na Seção B pergunta Telefone.**")

	elif telefone_duracao == "Selecione":
		st.write("**Correção necessária:**")
		st.write("**Selecione uma resposta na Seção B pergunta Telefone duração.**")

	elif mouse == "Selecione":
		st.write("**Correção necessária:**")
		st.write("**Selecione uma resposta na Seção C pergunta Mouse.**")

	elif mouse_duracao == "Selecione":
		st.write("**Correção necessária:**")
		st.write("**Selecione uma resposta na Seção C pergunta Mouse duração.**")

	elif teclado == "Selecione":
		st.write("**Correção necessária:**")
		st.write("**Selecione uma resposta na Seção C pergunta Teclado.**")

	elif teclado_duracao == "Selecione":
		st.write("**Correção necessária:**")
		st.write("**Selecione uma resposta na Seção C pergunta Teclado duração.**")

	df = pd.DataFrame(data)

	if "Selecione"  not in {altura_do_assento, profundidade_do_assento, descanso_de_braco,
	suporte_para_as_costas, secao_A_duracao, monitor, monitor_duracao, telefone, telefone_duracao,
	mouse, mouse_duracao, teclado, teclado_duracao }:


		df["Altura do assento: Sec A ROSA - altura do assento"] = lista_altura_do_assento_valida
		df["Profundidade do assento. Sec A ROSA - profundidade do assento"] = lista_profundidade_do_assento_valida
		df["Descanso de braço. Sec A ROSA - descanso de braço"] = lista_descanso_de_braco
		df["Suporte para as costas. Sec A ROSA - suporte para as costas"] = suporte_para_as_costas
		df["Seção A duração - ROSA:"] = lista_secao_A_duracao

		df["Monitor. Sec B ROSA - monitor"] = lista_monitor
		df["Seção B monitor duração - ROSA:"] = lista_monitor_duracao

		df["Telefone. Sec B ROSA - telefone"] = lista_telefone
		df["Seção B telefone duração - ROSA:"] = lista_telefone_duracao

		df["Mouse. Sec C ROSA - mouse"] = lista_mouse
		df["Seção C mouse duração - ROSA:"] = lista_mouse_duracao

		df["Seção C teclado duração - ROSA:"] = lista_teclado_duracao
		df["Teclado. Sec C ROSA - teclado"] = lista_teclado

		#VOltar aqui
		#st.write(df.T)

		
		colunas = list(df.columns)

		altura_do_assento_sec_a_rosa_altura_do_assento = []
		descanso_de_braco_sec_a_rosa_descanso_de_braco = []
		monitor_sec_b_rosa_monitor = []
		mouse_sec_c_rosa_mouse = []
		profundidade_do_assento_sec_a_rosa_profundidade_do_assento = []
		secao_a_duracao_rosa = []
		secao_b_monitor_duracao_rosa = []
		secao_b_telefone_duracao_rosa = []
		secao_c_mouse_duracao_rosa = []
		secao_c_teclado_duracao_rosa = []
		suporte_para_as_costas_sec_a_rosa_suporte_para_as_costas = []
		teclado_sec_c_rosa_teclado = []
		telefone_sec_b_rosa_telefone = []

		for x in colunas:
		    
		    if "Altura do assento: Sec A ROSA - altura do assento" in x:
		        altura_do_assento_sec_a_rosa_altura_do_assento.append(x)

		    elif "Descanso de braço. Sec A ROSA - descanso de braço" in x:
		        descanso_de_braco_sec_a_rosa_descanso_de_braco.append(x)

		    elif "Monitor. Sec B ROSA - monitor" in x:
		        monitor_sec_b_rosa_monitor.append(x)

		    elif "Mouse. Sec C ROSA - mouse" in x:
		        mouse_sec_c_rosa_mouse.append(x)

		    elif "Profundidade do assento. Sec A ROSA - profundidade do assento" in x:
		        profundidade_do_assento_sec_a_rosa_profundidade_do_assento.append(x)

		    elif "Seção A duração - ROSA:" in x:
		        secao_a_duracao_rosa.append(x)

		    elif "Seção B monitor duração - ROSA:" in x:
		        secao_b_monitor_duracao_rosa.append(x)

		    elif "Seção B telefone duração - ROSA:" in x:
		        secao_b_telefone_duracao_rosa.append(x)

		    elif "Seção C mouse duração - ROSA:" in x:
		        secao_c_mouse_duracao_rosa.append(x)

		    elif "Seção C teclado duração - ROSA:" in x:
		        secao_c_teclado_duracao_rosa.append(x)

		    elif "Suporte para as costas. Sec A ROSA - suporte para as costas" in x:
		        suporte_para_as_costas_sec_a_rosa_suporte_para_as_costas.append(x)

		    elif "Teclado. Sec C ROSA - teclado" in x:
		        teclado_sec_c_rosa_teclado.append(x)

		    elif "Telefone. Sec B ROSA - telefone" in x:
		        telefone_sec_b_rosa_telefone.append(x)


		# Altura do assento: Sec A ROSA - altura do assento

		# Montagem do DF por Seção
		df_sec_a_altura_do_assento = df.copy()
		df_sec_a_altura_do_assento = df_sec_a_altura_do_assento[[altura_do_assento_sec_a_rosa_altura_do_assento[0]]]

		# Coletando os valores respostas
		resultados_sec_a_altura_do_assento = []

		for x in df_sec_a_altura_do_assento["Altura do assento: Sec A ROSA - altura do assento"]:    
		    try:  # Se tem mais de um valor como resultado  
		        x = x.split(";")
		        for y in x:
		            y = y.strip()
		            resultados_sec_a_altura_do_assento.append(y)
		    except:
		        for y in x:
		            y = y.strip()
		            resultados_sec_a_altura_do_assento.append(y)

		# Score # Sec A - Altura do assento
		score_sec_a_altura_do_assento = []

		for x in resultados_sec_a_altura_do_assento:    
		    if 'Joelhos à 90° (1)' in x:
		        score_sec_a_altura_do_assento.append(1)
		        
		    elif 'Muito Baixo - Joelhos< 90° (2)' in x:
		        score_sec_a_altura_do_assento.append(2)
		        
		    elif 'Muito Alto - Joelhos> 90° (2)' in x:
		        score_sec_a_altura_do_assento.append(3)
		        
		    elif 'Pés sem contato com o chão(3)' in x:
		        score_sec_a_altura_do_assento.append(3)
		        
		    elif 'Espaço insuficiente embaixo da mesa (+1)' in x:
		        score_sec_a_altura_do_assento.append(1)
		        
		    elif 'Altura não ajustável (+1)' in x:
		        score_sec_a_altura_do_assento.append(1)

		score_sec_a_altura_do_assento = sum(score_sec_a_altura_do_assento)


		# Sec A - Profundidade do assento

		df_sec_a_profundidade_do_assento = df.copy()
		df_sec_a_profundidade_do_assento = df_sec_a_profundidade_do_assento[[profundidade_do_assento_sec_a_rosa_profundidade_do_assento[0]]]

		# Coletando os valores respostas
		resultados_sec_a_profundidade_do_assento = []

		for x in df_sec_a_profundidade_do_assento["Profundidade\xa0do assento. Sec A ROSA - profundidade do assento"]:    
		    try:  # Se tem mais de um valor como resultado  
		        x = x.split(";")
		        for y in x:
		            y = y.strip()
		            resultados_sec_a_profundidade_do_assento.append(y)
		    except:
		        for y in x:
		            y = y.strip()
		            resultados_sec_a_profundidade_do_assento.append(y)


		# Score # Sec A - profundidade_do_assento
		score_sec_a_profundidade_do_assento = []

		for x in resultados_sec_a_profundidade_do_assento:    
		    if 'Aprox. 7,5 cm entre joelho e final da cadeira (1)' in x:
		        score_sec_a_profundidade_do_assento.append(1)
		        
		    elif 'Muito próximo - espaço' in x:
		        score_sec_a_profundidade_do_assento.append(2)
		        
		    elif 'Muito distante - espaço >7,5 cm (2)' in x:
		        score_sec_a_profundidade_do_assento.append(2)
		        
		    elif 'Não ajustável (+1)' in x:
		        score_sec_a_profundidade_do_assento.append(1)

		score_sec_a_profundidade_do_assento = sum(score_sec_a_profundidade_do_assento)  
		 
		# Sec A - Descanso do braco
		df_sec_a_descanso_de_braco = df.copy()
		df_sec_a_descanso_de_braco = df_sec_a_descanso_de_braco[[descanso_de_braco_sec_a_rosa_descanso_de_braco[0]]]

		# Coletando os valores respostas
		resultados_sec_a_descanso_de_braco = []

		for x in df_sec_a_descanso_de_braco["Descanso de braço. Sec A ROSA - descanso de braço"]:    
		    try:  # Se tem mais de um valor como resultado  
		        x = x.split(";")
		        for y in x:
		            y = y.strip()
		            resultados_sec_a_descanso_de_braco.append(y)
		    except:
		        for y in x:
		            y = y.strip()
		            resultados_sec_a_descanso_de_braco.append(y)


		# Score # Sec A - Descanso braço
		score_sec_a_descanso_de_braco = []

		for x in resultados_sec_a_descanso_de_braco:    
		    if 'Suporte doombro alinhado com cotovelo - ombro relaxado (1)' in x:
		        score_sec_a_descanso_de_braco.append(1)
		        
		    elif 'Muito alto (ombros abduzidos)/ Baixo (braço sem suporte) (2)' in x:
		        score_sec_a_descanso_de_braco.append(2)
		        
		    elif 'Superfície escorregadia ou danificada (+1)' in x:
		        score_sec_a_descanso_de_braco.append(1)
		        
		    elif 'Muito Largo (+1)' in x:
		        score_sec_a_descanso_de_braco.append(1)
		    
		    elif 'Não ajustável (+1)' in x:
		        score_sec_a_descanso_de_braco.append(1)

		score_sec_a_descanso_de_braco = sum(score_sec_a_descanso_de_braco) 

		# Sec A - Suport para as costas
		df_sec_a_suporte_para_as_costas = df.copy()
		df_sec_a_suporte_para_as_costas = df_sec_a_suporte_para_as_costas[[suporte_para_as_costas_sec_a_rosa_suporte_para_as_costas[0]]]

		# Coletando os valores respostas
		resultados_sec_a_suporte_para_as_costas = []
		for x in df_sec_a_suporte_para_as_costas["Suporte para as costas. Sec A ROSA - suporte para as costas"]:
		    
		    try:  # Se tem mais de um valor como resultado  
		        x = x.split(";")
		        for y in x:
		            y = y.strip()
		            resultados_sec_a_suporte_para_as_costas.append(y)
		    except:
		        for y in x:
		            y = y.strip()
		            resultados_sec_a_suporte_para_as_costas.append(y)


		# Dando gerando o score final
		# Score # Sec A - profundidade_do_assento
		score_sec_a_suporte_para_as_costas = []

		for x in resultados_sec_a_suporte_para_as_costas:    
		    if 'Apoio lombar correto - cadeira reclinada entre95-110° (1)' in x:
		        score_sec_a_suporte_para_as_costas.append(1)
		        
		    elif 'Sem apoio lombar OU suporte não corretamentena parte inferior das costas (2)' in x:
		        score_sec_a_suporte_para_as_costas.append(2)
		        
		    elif 'Muito para trás(>110°) / Muito para frente (< 95°) (2)' in x:
		        score_sec_a_suporte_para_as_costas.append(2)
		        
		    elif 'Sem suporte para costas (banco)/ Trabalho de leituras com tronco parafrente (2)' in x:
		        score_sec_a_suporte_para_as_costas.append(2)
		    
		    elif 'Área de trabalho muito alta (ombros abduzidos)\xa0 (+1)' in x:
		        score_sec_a_suporte_para_as_costas.append(1)
		        
		    elif 'Apoio lombar sem ajustes (+1)' in x:
		        score_sec_a_suporte_para_as_costas.append(1)

		score_sec_a_suporte_para_as_costas = sum(score_sec_a_suporte_para_as_costas) 

		# Duração SEC A
		df_sec_a_duracao_rosa = df.copy()
		df_sec_a_duracao_rosa = df_sec_a_duracao_rosa[[secao_a_duracao_rosa[0]]]

		score_sec_a_duracao_rosa = []

		for x in df_sec_a_duracao_rosa["Seção A duração - ROSA:"]:
		    
		    if x == '> 1 h de forma continua ou mais que 4 h por dia (+1)':
		        score_sec_a_duracao_rosa.append(1)
		        
		    elif x == "Entre 30 min a 1 h de forma continua ou entre 1 e 4 h por dia (0)":
		        score_sec_a_duracao_rosa.append(0)
		        
		    elif x == "< 30 minutos de forma contínua, ou menos do que uma hora por dia (-1)":
		        score_sec_a_duracao_rosa.append(-1)        
		        
		score_sec_a_duracao_rosa = score_sec_a_duracao_rosa[0]

		#MAtriz ROSA
		# Secao A ==== Arms / Back res --- Seat Pan Height - Depth
		indice = [2,3,4,5,6,7,8]

		row_a = [1,2,3,4,5,6,7]
		row_b = [2,2,3,4,5,6,7]
		row_c = [3,3,3,4,5,6,7]
		row_d = [4,4,4,4,5,7,8]
		row_e = [5,5,5,5,5,7,8]
		row_f = [6,6,7,7,8,8,9]
		row_g = [7,7,7,7,8,9,9]
		row_h = [8,8,8,8,9,9,9]

		df_matriz_rosa_sec_a = pd.DataFrame()
		df_matriz_rosa_sec_a["2"] = row_a
		df_matriz_rosa_sec_a["3"] = row_b
		df_matriz_rosa_sec_a["4"] = row_c
		df_matriz_rosa_sec_a["5"] = row_d
		df_matriz_rosa_sec_a["6"] = row_e
		df_matriz_rosa_sec_a["7"] = row_f
		df_matriz_rosa_sec_a["8"] = row_g
		df_matriz_rosa_sec_a["9"] = row_h

		df_matriz_rosa_sec_a.index = indice


		# Na matriz é o ROW
		score_altura_e_prof_assento = score_sec_a_altura_do_assento + score_sec_a_profundidade_do_assento

		# Na matriz é a COLUNAS
		score_desc_braco_e_suporte_costas = score_sec_a_descanso_de_braco + score_sec_a_suporte_para_as_costas

		# Teste
		#score_altura_e_prof_assento = 4
		#score_desc_braco_e_suporte_costas = 4

		score_tmp_sec_a = df_matriz_rosa_sec_a.at[score_altura_e_prof_assento,str(score_desc_braco_e_suporte_costas)]
		score_final_sec_a = score_tmp_sec_a + score_sec_a_duracao_rosa # Soma com a duracao da Secaa A    



		# Seção B

		# Montagem do DF por Seção
		df_sec_b_monitor = df.copy()
		df_sec_b_monitor = df_sec_b_monitor[[monitor_sec_b_rosa_monitor[0]]]

		# Coletando os valores respostas
		resultados_sec_b_monitor = []

		for x in df_sec_b_monitor['Monitor. Sec B ROSA - monitor']:
		    
		    try:  # Se tem mais de um valor como resultado  
		        x = x.split(";")
		        for y in x:
		            y = y.strip()
		            resultados_sec_b_monitor.append(y)
		    except:
		        for y in x:
		            y = y.strip()
		            resultados_sec_b_monitor.append(y)

		score_sec_b_monitor = []

		for x in resultados_sec_b_monitor:
		    
		    if 'Distância de um braço (40 - 75 cm) / Monitor na altura dos olhos (1)' in x:
		        score_sec_b_monitor.append(1)
		        
		    elif 'Muito perto (< 30°)(2)' in x:
		        score_sec_b_monitor.append(2)
		        
		    elif 'Muito Alto - cabeça em extensão(3)' in x:
		        score_sec_b_monitor.append(3)
		        
		    elif 'Cabeça rodada maior que 30° (+1)' in x:
		        score_sec_b_monitor.append(1)
		    
		    elif 'Brilho na tela (+1)' in x:
		        score_sec_b_monitor.append(1)
		        
		    elif 'Sem porta documentos (+1)' in x:
		        score_sec_b_monitor.append(1)

		    elif 'Muito longe (+1)' in x:
		        score_sec_b_monitor.append(1)

		score_sec_b_monitor = sum(score_sec_b_monitor) 


		# Telefone
		df_sec_b_telefone = df.copy()
		df_sec_b_telefone = df_sec_b_telefone[[telefone_sec_b_rosa_telefone[0]]]

		# Coletando os valores respostas
		resultados_sec_b_telefone = []

		for x in df_sec_b_telefone['Telefone. Sec B ROSA - telefone']:
		    
		    try:  # Se tem mais de um valor como resultado  
		        x = x.split(";")
		        for y in x:
		            y = y.strip()
		            resultados_sec_b_telefone.append(y)
		    except:
		        for y in x:
		            y = y.strip()
		            resultados_sec_b_telefone.append(y)


		score_sec_b_telefone = []

		for x in resultados_sec_b_telefone:
		    
		    if 'Headset /Uma mão no telefone e pescoço em posição neutra (1)' in x:
		        score_sec_b_telefone.append(1)
		        
		    elif 'Muito longe para atender (> 30 cm) (2)' in x:
		        score_sec_b_telefone.append(2)
		        
		    elif 'Segurando com cabeça e ombro (+2)' in x:
		        score_sec_b_telefone.append(2)
		        
		    elif 'Sem opção de mãos livres (handset) (+1)' in x:
		        score_sec_b_telefone.append(1)

		score_sec_b_telefone = sum(score_sec_b_telefone) 


		# Duração SEC B - Duracao telefone
		df_sec_b_duracao_telefone = df.copy()
		df_sec_b_duracao_telefone = df_sec_b_duracao_telefone[[secao_b_telefone_duracao_rosa[0]]]

		score_sec_b_duracao_telefone = []

		for x in df_sec_b_duracao_telefone['Seção B telefone duração - ROSA:']:
		    
		    if x == '> 1 h de forma continua ou mais que 4 h por dia (+1)':
		        score_sec_b_duracao_telefone.append(1)
		        
		    elif x == "Entre 30 min a 1 h de forma continua ou entre 1 e 4 h por dia (0)":
		        score_sec_b_duracao_telefone.append(0)
		        
		    elif x == "< 30 minutos de forma contínua, ou menos do que uma hora por dia (-1)":
		        score_sec_b_duracao_telefone.append(-1)        
		        
		score_sec_b_duracao_telefone = score_sec_b_duracao_telefone[0]


		# Duração SEC B - Duracao telefone
		df_sec_b_duracao_monitor = df.copy()
		df_sec_b_duracao_monitor = df_sec_b_duracao_monitor[[secao_b_monitor_duracao_rosa[0]]]

		score_sec_b_duracao_monitor = []

		for x in df_sec_b_duracao_monitor['Seção B monitor duração - ROSA:']:    
		    x = x.strip()    
		    if x == '> 1 h de forma continua ou mais que 4 h por dia (+1)':
		        score_sec_b_duracao_monitor.append(1)
		        
		    elif x == "Entre 30 min a 1 h de forma continua ou entre 1 e 4 h por dia (0)":
		        score_sec_b_duracao_monitor.append(0)
		        
		    elif x == "< 30 minutos de forma contínua, ou menos do que uma hora por dia (-1)":
		        score_sec_b_duracao_monitor.append(-1)        
		        
		score_sec_b_duracao_monitor = score_sec_b_duracao_monitor[0]

		#MAtriz ROSA
		# Secao B ==== MOnitor --- Phone
		indice = [0,1,2,3,4,5,6]

		row_a = [1,1,1,2,3,4,5]
		row_b = [1,1,2,2,3,4,5]
		row_c = [1,2,2,3,4,5,6]
		row_d = [2,2,3,3,4,5,7]
		row_e = [3,3,3,4,5,6,8]
		row_f = [4,4,4,5,6,7,8]
		row_g = [5,5,6,6,7,8,9]
		row_h = [6,6,7,8,8,9,9]

		df_matriz_rosa_sec_b = pd.DataFrame()
		df_matriz_rosa_sec_b["0"] = row_a
		df_matriz_rosa_sec_b["1"] = row_b
		df_matriz_rosa_sec_b["2"] = row_c
		df_matriz_rosa_sec_b["3"] = row_d
		df_matriz_rosa_sec_b["4"] = row_e
		df_matriz_rosa_sec_b["5"] = row_f
		df_matriz_rosa_sec_b["6"] = row_g
		df_matriz_rosa_sec_a["7"] = row_h


		df_matriz_rosa_sec_b.index = indice


		# Na matriz é o ROW
		score_telefone = score_sec_b_monitor + score_sec_b_duracao_monitor

		# Na matriz é a COLUNAS
		score_monitor = score_sec_b_telefone + score_sec_b_duracao_telefone

		# Teste
		#score_monitor = 2
		#score_telefone = 3

		score_final_sec_b = df_matriz_rosa_sec_b.at[score_telefone,str(score_monitor)]



		# Seção C
		# Montagem do DF por Seção
		df_sec_c_mouse = df.copy()
		df_sec_c_mouse = df_sec_c_mouse[[mouse_sec_c_rosa_mouse[0]]]
		

		# Coletando os valores respostas
		resultados_sec_c_mouse = []

		for x in df_sec_c_mouse['Mouse. Sec C ROSA - mouse']:    
		    try:  # Se tem mais de um valor como resultado  
		        x = x.split(";")
		        for y in x:
		            y = y.strip()
		            resultados_sec_c_mouse.append(y)
		    except:
		        for y in x:
		            y = y.strip()
		            resultados_sec_c_mouse.append(y)

		score_sec_c_mouse = []

		for x in resultados_sec_c_mouse:
		    
		    if 'Mouse alinhado com o ombro (1)' in x:
		        score_sec_c_mouse.append(1)
		        
		    elif 'Mouse afastado / distanteda linha do ombro (2)' in x:
		        score_sec_c_mouse.append(2)
		        
		    elif 'Mouse e teclado em superfícies diferentes (+2)' in x:
		        score_sec_c_mouse.append(2)
		        
		    elif 'Mouse pequeno (mão em garra) (+1)' in x:
		        score_sec_c_mouse.append(1)
		    
		    elif 'Apoio de punho em frente ao mouse (+1)' in x:
		        score_sec_c_mouse.append(1)        

		score_sec_c_mouse = sum(score_sec_c_mouse) 


		# Duração SEC C - Duracao MOUSE
		df_sec_c_duracao_mouse = df.copy()
		df_sec_c_duracao_mouse = df_sec_c_duracao_mouse[[secao_c_mouse_duracao_rosa[0]]]

		score_sec_c_duracao_mouse = []

		for x in df_sec_c_duracao_mouse['Seção C mouse duração - ROSA:']:
		    
		    if x == '> 1 h de forma continua ou mais que 4 h por dia (+1)':
		        score_sec_c_duracao_mouse.append(1)
		        
		    elif x == "Entre 30 min a 1 h de forma continua ou entre 1 e 4 h por dia (0)":
		        score_sec_c_duracao_mouse.append(0)
		        
		    elif x == "< 30 minutos de forma contínua, ou menos do que uma hora por dia (-1)":
		        score_sec_c_duracao_mouse.append(-1)        
		        
		score_sec_c_duracao_mouse = score_sec_c_duracao_mouse[0]


		# Teclado
		df_sec_c_teclado = df.copy()
		df_sec_c_teclado = df_sec_c_teclado[[teclado_sec_c_rosa_teclado[0]]]


		# Coletando os valores respostas
		resultados_sec_c_teclado = []

		for x in df_sec_c_teclado['Teclado. Sec C ROSA - teclado']:    
		    try:  # Se tem mais de um valor como resultado  
		        x = x.split(";")
		        for y in x:
		            y = y.strip()
		            resultados_sec_c_teclado.append(y)
		    except:
		        for y in x:
		            y = y.strip()
		            resultados_sec_c_teclado.append(y)

		score_sec_c_teclado = []

		for x in resultados_sec_c_teclado:
		    
		    if 'Pulsos neutros /Ombros relaxados (1)' in x:
		        score_sec_c_teclado.append(1)
		        
		    elif 'Punhos extendidos \xa0/ Teclado com angulo positivo (>15°) (2)' in x:
		        score_sec_c_teclado.append(2)
		        
		    elif 'Desvio de punho ao digitar(+1)' in x:
		        score_sec_c_teclado.append(1)
		        
		    elif 'Teclado alto / ombros abduzidos (+1)' in x:
		        score_sec_c_teclado.append(1)
		    
		    elif 'Pegar coisas acima da cabeça (+1)' in x:
		        score_sec_c_teclado.append(1)
		        
		    elif 'Mesa não ajustavél(+1)' in x:
		        score_sec_c_teclado.append(1)   

		score_sec_c_teclado = sum(score_sec_c_teclado) 

		# Duração SEC C - Duracao TECLADO
		df_sec_c_duracao_teclado = df.copy()
		df_sec_c_duracao_teclado = df_sec_c_duracao_teclado[[secao_c_teclado_duracao_rosa[0]]]


		score_sec_c_duracao_teclado = []

		for x in df_sec_c_duracao_teclado['Seção C teclado duração - ROSA:']:  
		    
		    if x == '> 1 h de forma continua ou mais que 4 h por dia (+1)':
		        score_sec_c_duracao_teclado.append(1)
		        
		    elif x == "Entre 30 min a 1 h de forma continua ou entre 1 e 4 h por dia (0)":
		        score_sec_c_duracao_teclado.append(0)
		        
		    elif x == "< 30 minutos de forma contínua, ou menos do que uma hora por dia (-1)":
		        score_sec_c_duracao_teclado.append(-1)        
		        
		score_sec_c_duracao_teclado = score_sec_c_duracao_teclado[0]

		#MAtriz ROSA
		# Secao C ==== Teclado e mouse
		indice = [0,1,2,3,4,5,6,7]

		row_a = [1,1,1,2,3,4,5,6]
		row_b = [1,1,2,3,4,5,6,7]
		row_c = [1,2,2,3,4,5,6,7]
		row_d = [2,3,3,3,5,6,7,8]
		row_e = [3,4,4,5,5,6,7,8]
		row_f = [4,5,5,6,6,7,8,9]
		row_g = [5,6,6,7,7,8,8,9]
		row_h = [6,7,7,8,8,9,9,9]

		df_matriz_rosa_sec_c = pd.DataFrame()
		df_matriz_rosa_sec_c["0"] = row_a
		df_matriz_rosa_sec_c["1"] = row_b
		df_matriz_rosa_sec_c["2"] = row_c
		df_matriz_rosa_sec_c["3"] = row_d
		df_matriz_rosa_sec_c["4"] = row_e
		df_matriz_rosa_sec_c["5"] = row_f
		df_matriz_rosa_sec_c["6"] = row_g
		df_matriz_rosa_sec_c["7"] = row_h

		df_matriz_rosa_sec_c.index = indice

		# Na matriz é o ROW
		score_mouse = score_sec_c_mouse + score_sec_c_duracao_mouse

		# Na matriz é a COLUNAS
		score_teclado = score_sec_c_teclado + score_sec_c_duracao_teclado

		# Teste
		#score_teclado = 2
		#score_mouse = 2

		score_final_sec_c = df_matriz_rosa_sec_c.at[score_mouse,str(score_teclado)]
		#score_final_sec_c



		# Perifericos
		# Matriz
		# Monitor e score d eperiferico
		# Mouse e teclado / Monitor e telefone
		indice = [1,2,3,4,5,6,7,8,9]

		row_a = [1,2,3,4,5,6,7,8,9]
		row_b = [2,2,3,4,5,6,7,8,9]
		row_c = [3,3,3,4,5,6,7,8,9]
		row_d = [4,4,4,4,5,6,7,8,9]
		row_e = [5,5,5,5,5,6,7,8,9]
		row_f = [6,6,6,6,6,6,7,8,9]
		row_g = [7,7,7,7,7,7,7,8,9]
		row_h = [8,8,8,8,8,8,8,8,9]
		row_i = [9,9,9,9,9,9,9,9,9]
		row_j = [10,10,10,10,10,10,10,10,10]

		df_matriz_monitor_e_score_de_perife = pd.DataFrame()
		df_matriz_monitor_e_score_de_perife["1"] = row_a
		df_matriz_monitor_e_score_de_perife["2"] = row_b
		df_matriz_monitor_e_score_de_perife["3"] = row_c
		df_matriz_monitor_e_score_de_perife["4"] = row_d
		df_matriz_monitor_e_score_de_perife["5"] = row_e
		df_matriz_monitor_e_score_de_perife["6"] = row_f
		df_matriz_monitor_e_score_de_perife["7"] = row_g
		df_matriz_monitor_e_score_de_perife["8"] = row_h
		df_matriz_monitor_e_score_de_perife["9"] = row_i

		df_matriz_monitor_e_score_de_perife.index = indice
		


		# A selecao da coluna dessa matriz é a variavel score_final_sec_c
		# A selecao do row dessa matriz é a variavel score_final_sec_b
		# Fonte: https://www.youtube.com/watch?v=-S7Scpdk194
		# vídeo: 8.38

		score_matriz_monitor_e_score_de_perife = df_matriz_monitor_e_score_de_perife.at[score_final_sec_b,str(score_final_sec_c)]

		# Periféricos e monitor / cadeira
		indice = [1,2,3,4,5,6,7,8,9,10]

		row_a = [1,2,3,4,5,6,7,8,9,10]
		row_b = [2,2,3,4,5,6,7,8,9,10]
		row_c = [3,3,3,4,5,6,7,8,9,10]
		row_d = [4,4,4,4,5,6,7,8,9,10]
		row_e = [5,5,5,5,5,6,7,8,9,10]
		row_f = [6,6,6,6,6,6,7,8,9,10]
		row_g = [7,7,7,7,7,7,7,8,9,10]
		row_h = [8,8,8,8,8,8,8,8,9,10]
		row_i = [9,9,9,9,9,9,9,9,9,10]
		row_j = [10,10,10,10,10,10,10,10,10,10]

		df_matriz_perifierico_e_monitor = pd.DataFrame()
		df_matriz_perifierico_e_monitor["1"] = row_a
		df_matriz_perifierico_e_monitor["2"] = row_b
		df_matriz_perifierico_e_monitor["3"] = row_c
		df_matriz_perifierico_e_monitor["4"] = row_d
		df_matriz_perifierico_e_monitor["5"] = row_e
		df_matriz_perifierico_e_monitor["6"] = row_f
		df_matriz_perifierico_e_monitor["7"] = row_g
		df_matriz_perifierico_e_monitor["8"] = row_h
		df_matriz_perifierico_e_monitor["9"] = row_i
		df_matriz_perifierico_e_monitor["10"] = row_j

		df_matriz_perifierico_e_monitor.index = indice

		# A selecao da coluna dessa matriz é a variavel score_matriz_monitor_e_score_de_perife
		# A selecao do row dessa matriz é a variavel score_final_sec_a
		# Fonte: https://www.youtube.com/watch?v=-S7Scpdk194
		# vídeo: 8.38

		#score_final_sec_a = 4
		#score_matriz_monitor_e_score_de_perife = 3

		rosa_final_score = df_matriz_perifierico_e_monitor.at[score_final_sec_a,str(score_matriz_monitor_e_score_de_perife)]


		def rosa_final_score_categoria(score):
		    
		    if score <= 4:
		        return "Baixo risco"
		    
		    elif score >= 5 and score < 7:
		        return "Risco moderado"
		    
		    else:
		        return "Alto risco" 
		    
		rosa_final_score_cat = rosa_final_score_categoria(rosa_final_score)



		# Preparado arquivo do TESTE, resultado
		df_sec_a_altura_do_assento_tranpose = df_sec_a_altura_do_assento.T
		df_sec_a_profundidade_do_assento_tranpose = df_sec_a_profundidade_do_assento.T
		df_sec_a_descanso_de_braco_tranpose = df_sec_a_descanso_de_braco.T
		df_sec_a_suporte_para_as_costas_tranpose = df_sec_a_suporte_para_as_costas.T
		df_sec_a_duracao_rosa_tranpose = df_sec_a_duracao_rosa.T
		df_sec_b_monitor_tranpose = df_sec_b_monitor.T
		df_sec_b_telefone_tranpose = df_sec_b_telefone.T
		df_sec_b_duracao_monitor_tranpose = df_sec_b_duracao_monitor.T
		df_sec_b_duracao_telefone_tranpose = df_sec_b_duracao_telefone.T
		df_sec_c_mouse_tranpose = df_sec_c_mouse.T
		df_sec_c_duracao_mouse_tranpose = df_sec_c_duracao_mouse.T
		df_sec_c_teclado_tranpose = df_sec_c_teclado.T
		df_sec_c_duracao_teclado_tranpose = df_sec_c_duracao_teclado.T

		df_sec_a_altura_do_assento_tranpose = df_sec_a_altura_do_assento_tranpose.reset_index(drop=False)
		df_sec_a_profundidade_do_assento_tranpose = df_sec_a_profundidade_do_assento_tranpose.reset_index(drop=False)
		df_sec_a_descanso_de_braco_tranpose = df_sec_a_descanso_de_braco_tranpose.reset_index(drop=False)
		df_sec_a_suporte_para_as_costas_tranpose = df_sec_a_suporte_para_as_costas_tranpose.reset_index(drop=False)
		df_sec_a_duracao_rosa_tranpose = df_sec_a_duracao_rosa_tranpose.reset_index(drop=False)
		df_sec_b_monitor_tranpose = df_sec_b_monitor_tranpose.reset_index(drop=False)
		df_sec_b_telefone_tranpose = df_sec_b_telefone_tranpose.reset_index(drop=False)
		df_sec_b_duracao_monitor_tranpose = df_sec_b_duracao_monitor_tranpose.reset_index(drop=False)
		df_sec_b_duracao_telefone_tranpose = df_sec_b_duracao_telefone_tranpose.reset_index(drop=False)
		df_sec_c_mouse_tranpose = df_sec_c_mouse_tranpose.reset_index(drop=False)
		df_sec_c_duracao_mouse_tranpose = df_sec_c_duracao_mouse_tranpose.reset_index(drop=False)
		df_sec_c_teclado_tranpose = df_sec_c_teclado_tranpose.reset_index(drop=False)
		df_sec_c_duracao_teclado_tranpose = df_sec_c_duracao_teclado_tranpose.reset_index(drop=False)

		df_sec_a_altura_do_assento_tranpose = df_sec_a_altura_do_assento_tranpose.rename(columns={"index":"Perguntas",0:"Respostas"})
		df_sec_a_profundidade_do_assento_tranpose = df_sec_a_profundidade_do_assento_tranpose.rename(columns={"index":"Perguntas",0:"Respostas"})
		df_sec_a_descanso_de_braco_tranpose = df_sec_a_descanso_de_braco_tranpose.rename(columns={"index":"Perguntas",0:"Respostas"})
		df_sec_a_suporte_para_as_costas_tranpose = df_sec_a_suporte_para_as_costas_tranpose.rename(columns={"index":"Perguntas",0:"Respostas"})
		df_sec_a_duracao_rosa_tranpose = df_sec_a_duracao_rosa_tranpose.rename(columns={"index":"Perguntas",0:"Respostas"})
		df_sec_b_monitor_tranpose = df_sec_b_monitor_tranpose.rename(columns={"index":"Perguntas",0:"Respostas"})
		df_sec_b_telefone_tranpose = df_sec_b_telefone_tranpose.rename(columns={"index":"Perguntas",0:"Respostas"})
		df_sec_b_duracao_monitor_tranpose = df_sec_b_duracao_monitor_tranpose.rename(columns={"index":"Perguntas",0:"Respostas"})
		df_sec_b_duracao_telefone_tranpose = df_sec_b_duracao_telefone_tranpose.rename(columns={"index":"Perguntas",0:"Respostas"})
		df_sec_c_mouse_tranpose = df_sec_c_mouse_tranpose.rename(columns={"index":"Perguntas",0:"Respostas"})
		df_sec_c_duracao_mouse_tranpose = df_sec_c_duracao_mouse_tranpose.rename(columns={"index":"Perguntas",0:"Respostas"})
		df_sec_c_teclado_tranpose = df_sec_c_teclado_tranpose.rename(columns={"index":"Perguntas",0:"Respostas"})
		df_sec_c_duracao_teclado_tranpose = df_sec_c_duracao_teclado_tranpose.rename(columns={"index":"Perguntas",0:"Respostas"})



		df_resultado_rosa_out = pd.DataFrame()
		df_resultado_rosa_out = pd.concat([df_sec_a_altura_do_assento_tranpose,df_sec_a_profundidade_do_assento_tranpose,
		df_sec_a_descanso_de_braco_tranpose,df_sec_a_suporte_para_as_costas_tranpose,
		df_sec_a_duracao_rosa_tranpose,df_sec_b_monitor_tranpose,df_sec_b_telefone_tranpose,
		df_sec_b_duracao_monitor_tranpose,df_sec_b_duracao_telefone_tranpose,
		df_sec_c_mouse_tranpose,df_sec_c_duracao_mouse_tranpose,df_sec_c_teclado_tranpose,
		df_sec_c_duracao_teclado_tranpose], ignore_index=True)


		# Variaveis das pontuacoes das perguntas
		#score_sec_a_altura_do_assento,score_sec_a_profundidade_do_assento,score_sec_a_descanso_de_braco,
		#score_sec_a_suporte_para_as_costas,score_sec_a_duracao_rosa,score_sec_b_monitor,
		#score_sec_b_telefone,score_sec_b_duracao_monitor,score_sec_b_duracao_telefone,
		#score_sec_c_mouse,score_sec_c_duracao_mouse,score_sec_c_teclado,score_sec_c_duracao_teclado,


		pontuacao = []
		pontuacao.append(score_sec_a_altura_do_assento)
		pontuacao.append(score_sec_a_profundidade_do_assento)
		pontuacao.append(score_sec_a_descanso_de_braco)
		pontuacao.append(score_sec_a_suporte_para_as_costas)
		pontuacao.append(score_sec_a_duracao_rosa)
		pontuacao.append(score_sec_b_monitor)
		pontuacao.append(score_sec_b_telefone)
		pontuacao.append(score_sec_b_duracao_monitor)
		pontuacao.append(score_sec_b_duracao_telefone)
		pontuacao.append(score_sec_c_mouse)
		pontuacao.append(score_sec_c_duracao_mouse)
		pontuacao.append(score_sec_c_teclado)
		pontuacao.append(score_sec_c_duracao_teclado)
		df_resultado_rosa_out["Pontuação das repostas"] = pontuacao


		lista_de_scores_para_o_df = []
		lista_de_scores_para_o_df.append("")
		lista_de_scores_para_o_df.append("Score A (Cadeiras)")
		lista_de_scores_para_o_df.append(score_final_sec_a)

		df_resultado_rosa_out_length = len(df_resultado_rosa_out)
		df_resultado_rosa_out.loc[df_resultado_rosa_out_length] = lista_de_scores_para_o_df

		lista_de_scores_para_o_df = []
		lista_de_scores_para_o_df.append("")
		lista_de_scores_para_o_df.append("Score B (Monitor/Telefone)")
		lista_de_scores_para_o_df.append(score_final_sec_b)

		df_resultado_rosa_out_length = len(df_resultado_rosa_out)
		df_resultado_rosa_out.loc[df_resultado_rosa_out_length] = lista_de_scores_para_o_df

		lista_de_scores_para_o_df = []
		lista_de_scores_para_o_df.append("")
		lista_de_scores_para_o_df.append("Score C (Mouse/Teclado)")
		lista_de_scores_para_o_df.append(score_final_sec_c)

		df_resultado_rosa_out_length = len(df_resultado_rosa_out)
		df_resultado_rosa_out.loc[df_resultado_rosa_out_length] = lista_de_scores_para_o_df

		lista_de_scores_para_o_df = []
		lista_de_scores_para_o_df.append("")
		lista_de_scores_para_o_df.append("Score Periféricos")
		lista_de_scores_para_o_df.append(score_matriz_monitor_e_score_de_perife)

		df_resultado_rosa_out_length = len(df_resultado_rosa_out)
		df_resultado_rosa_out.loc[df_resultado_rosa_out_length] = lista_de_scores_para_o_df

		lista_de_scores_para_o_df = []
		lista_de_scores_para_o_df.append("")
		lista_de_scores_para_o_df.append("Score final")
		lista_de_scores_para_o_df.append(rosa_final_score)

		df_resultado_rosa_out_length = len(df_resultado_rosa_out)
		df_resultado_rosa_out.loc[df_resultado_rosa_out_length] = lista_de_scores_para_o_df

		lista_de_scores_para_o_df = []
		lista_de_scores_para_o_df.append("")
		lista_de_scores_para_o_df.append("Resultado")
		lista_de_scores_para_o_df.append(rosa_final_score_cat)

		df_resultado_rosa_out_length = len(df_resultado_rosa_out)
		df_resultado_rosa_out.loc[df_resultado_rosa_out_length] = lista_de_scores_para_o_df

		
		#st.write(df_resultado_rosa_out)
		st.write("**Resultado da análise:**")
		st.write("")

		st.write("**Pontuação das perguntas**")

		df_resultado_rosa_out_copia = df_resultado_rosa_out.copy()
		df_resultado_rosa_out_copia = df_resultado_rosa_out_copia.iloc[:13]
		st.table(df_resultado_rosa_out_copia)

		st.write("")

		st.write("**Score das Seções**")

		df_saida = df_resultado_rosa_out.iloc[13:]
		del df_saida["Perguntas"]
		st.table(df_saida)			

		st.title(f"**Resultado final: {df_saida.iloc[5]['Pontuação das repostas']}**")






