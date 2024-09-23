CREATE DATABASE ingestao;

\c ingestao

CREATE TABLE IF NOT EXISTS bancos (
	id SERIAL PRIMARY KEY,
	segmento VARCHAR(2),
	cnpj VARCHAR(20),
	nome VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS empregados (
	id SERIAL PRIMARY KEY,
	employer_name VARCHAR(255),
	reviews_count INTEGER,
	culture_count INTEGER,
	salaries_count INTEGER,
	benefits_count INTEGER,
	employer_website VARCHAR(255),
	employer_headquarters VARCHAR(255),
	employer_founded SMALLINT,
	employer_industry VARCHAR(100),
	employer_revenue VARCHAR(100),
	url VARCHAR(200),
	geral REAL,
	cultura_e_valores REAL,
	diversidade_e_inclusao REAL,
	qualidade_de_vida REAL,
	alta_lideranca REAL,
	remuneracao_e_beneficios REAL,
	oportunidades_de_carreira REAL,
	recomendam_para_outras_pessoas REAL,
	perspectiva_positiva_da_empresa REAL,
	cnpj VARCHAR(20),
	nome VARCHAR(255),
	match_percent SMALLINT,
	segmento VARCHAR(2)
	
);


CREATE TABLE IF NOT EXISTS reclamacoes (
        id SERIAL PRIMARY KEY,
        ano SMALLINT,
        trimestre VARCHAR(2),
        categoria VARCHAR(100),
        tipo VARCHAR(20),
	cnpj_if VARCHAR(20),
        Instituicao_financeira VARCHAR(255),
        Indice VARCHAR(10),
        quantidade_de_reclamacoes_reguladas_procedentes INTEGER,
        quantidade_de_reclamacoes_reguladas_outras INTEGER,
        quantidade_de_reclamacoes_nao_reguladas INTEGER,
        quantidade_total_de_reclamacoes INTEGER,
        quantidade_total_de_clientes_CCS_e_SCR VARCHAR(10),
        quantidade_de_cliente_CCS VARCHAR(10),
	quantidade_de_cliente_SCR VARCHAR(10),
        employer_name VARCHAR(255),
        reviews_count INTEGER,
        culture_count INTEGER,
        salaries_count INTEGER,
        benefits_count INTEGER,
        employer_website VARCHAR(255),
        employer_headquarters VARCHAR(255),
        employer_founded SMALLINT,
        employer_industry VARCHAR(100),
        employer_revenue VARCHAR(100),
        url VARCHAR(200),
        geral REAL,
        cultura_e_valores REAL,
        diversidade_e_inclusao REAL,
        qualidade_de_vida REAL,
        alta_lideranca Real,
        remuneracao_e_beneficios REAL,
        oportunidades_de_carreira REAL,
        recomendam_para_outras_pessoas REAL,
        perspectiva_positiva_da_empresa REAL,
        segmento VARCHAR(2),
        nome VARCHAR(255),
        match_percent SMALLINT,
        cnpj VARCHAR(30)
);
