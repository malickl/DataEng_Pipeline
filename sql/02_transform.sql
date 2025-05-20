/* ────────────────────────────────────────────────
   02_transform.sql
   - copie les lignes du staging vers le core
   - évite les doublons
   - fait un petit nettoyage de texte (trim/upper sur le pays)
   ────────────────────────────────────────────────*/

INSERT INTO core.services_bancaires AS tgt
(
    annee, pays, tranche_age, type_operation,
    nombre_utilisateurs, volume_transactions, valeur_transactions,
    taux_penetration_fintechs, service_fintech_populaire,
    bancarisation_traditionnelle, acces_internet_smartphone,
    revenu_moyen, frein_adoption
)
SELECT
    annee,
    INITCAP(TRIM(pays))                       AS pays,
    TRIM(tranche_age)                         AS tranche_age,
    TRIM(type_operation)                      AS type_operation,
    nombre_utilisateurs,
    volume_transactions,
    valeur_transactions,
    taux_penetration_fintechs,
    TRIM(service_fintech_populaire),
    bancarisation_traditionnelle,
    acces_internet_smartphone,
    revenu_moyen,
    TRIM(frein_adoption)
FROM stg.services_bancaires AS src
ON CONFLICT (annee, pays, tranche_age, type_operation) DO NOTHING;
