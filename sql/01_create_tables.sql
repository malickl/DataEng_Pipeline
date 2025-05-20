/* ────────────────────────────────────────────────
   01_create_tables.sql
   - crée les schémas stg (brut) et core (propre)
   - crée les deux tables nécessaires au pipeline
   ────────────────────────────────────────────────*/

-- 1. Schémas
CREATE SCHEMA IF NOT EXISTS stg;
CREATE SCHEMA IF NOT EXISTS core;

---------------------------------------------------
-- 2. Table STAGING : même structure que le CSV
---------------------------------------------------
DROP TABLE IF EXISTS stg.services_bancaires;
CREATE TABLE stg.services_bancaires (
    annee                          SMALLINT,
    pays                           TEXT,
    tranche_age                    TEXT,
    nombre_utilisateurs            BIGINT,
    volume_transactions            BIGINT,
    valeur_transactions            NUMERIC(18,2),
    type_operation                 TEXT,
    taux_penetration_fintechs      NUMERIC(5,2),
    service_fintech_populaire      TEXT,
    bancarisation_traditionnelle   NUMERIC(5,2),
    acces_internet_smartphone      NUMERIC(5,2),
    revenu_moyen                   BIGINT,
    frein_adoption                 TEXT
);

---------------------------------------------------
-- 3. Table CORE : données nettoyées / dé-doublonnées
---------------------------------------------------
DROP TABLE IF EXISTS core.services_bancaires;
CREATE TABLE core.services_bancaires (
    annee                          SMALLINT   NOT NULL,
    pays                           TEXT       NOT NULL,
    tranche_age                    TEXT       NOT NULL,
    type_operation                 TEXT       NOT NULL,
    nombre_utilisateurs            BIGINT,
    volume_transactions            BIGINT,
    valeur_transactions            NUMERIC(18,2),
    taux_penetration_fintechs      NUMERIC(5,2),
    service_fintech_populaire      TEXT,
    bancarisation_traditionnelle   NUMERIC(5,2),
    acces_internet_smartphone      NUMERIC(5,2),
    revenu_moyen                   BIGINT,
    frein_adoption                 TEXT,
    -- clé composite « métier » pour éviter les doublons :
    CONSTRAINT pk_srv PRIMARY KEY (annee, pays, tranche_age, type_operation)
);

-- 4. Index utile pour les analyses par pays/année
CREATE INDEX IF NOT EXISTS idx_srv_pays_annee
    ON core.services_bancaires (pays, annee);
