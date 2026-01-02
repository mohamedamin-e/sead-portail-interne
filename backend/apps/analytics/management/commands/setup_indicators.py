from django.core.management.base import BaseCommand
from analytics.models import Indicateur

class Command(BaseCommand):
    help = 'Initialise les 56 indicateurs SEAD à partir du manuel technique'

    def handle(self, *args, **options):
        # Liste complète des 56 indicateurs basés sur ton PDF
        indicators_data = [
            # I. CARACTÉRISTIQUES SOCIODÉMOGRAPHIQUES
            {'code': 'A1', 'libelle': 'Taille moyenne du ménage', 'type': 'Suivi', 'unite': 'Nombre', 'frequence': 'Annuelle', 'formule': 'Moyenne du nombre de personnes par ménage'},
            {'code': 'A2', 'libelle': 'Proportion de chefs de ménage femmes', 'type': 'Performance', 'unite': '%', 'frequence': 'Annuelle', 'formule': '(Nb chefs de ménage femmes / Total chefs de ménage) × 100'},
            {'code': 'A3', 'libelle': 'Structure par tranche d’âge', 'type': 'Suivi', 'unite': '%', 'frequence': 'Annuelle', 'formule': 'Répartition du ménage par catégories : 0–14, 15–24, 25–64, 65+'},
            {'code': 'A4', 'libelle': 'Niveau moyen d’éducation du chef de ménage', 'type': 'Performance', 'unite': 'Niveau', 'frequence': 'Annuelle', 'formule': 'Moyenne des années de scolarité ou niveau d’éducation atteint'},
            {'code': 'A5', 'libelle': 'Appartenance à coopératives ou associations', 'type': 'Suivi', 'unite': '%', 'frequence': 'Annuelle', 'formule': '% de ménages membres de coopératives agricoles ou associations'},

            # II. TYPOLOGIE DE L’EXPLOITATION
            {'code': 'A6', 'libelle': 'Nombre moyen de parcelles par exploitation', 'type': 'Suivi', 'unite': 'Parcelles', 'frequence': 'Saisonnière', 'formule': 'Moyenne du nombre de parcelles détenues par exploitation'},
            {'code': 'A7', 'libelle': 'Superficie moyenne par exploitation', 'type': 'Suivi', 'unite': 'ha', 'frequence': 'Annuelle', 'formule': 'Moyenne de la superficie totale des parcelles par exploitation'},
            {'code': 'A8', 'libelle': 'Taux de diversification des cultures', 'type': 'Performance', 'unite': '%', 'frequence': 'Saisonnière', 'formule': '(Exploitations avec ≥2 cultures / Total exploitations) × 100'},
            {'code': 'A9', 'libelle': 'Proportion d’exploitations mixtes (cultures + élevage)', 'type': 'Performance', 'unite': '%', 'frequence': 'Annuelle', 'formule': '(Exploitations mixtes / Total exploitations) × 100'},
            {'code': 'A10', 'libelle': 'Proportion de production destinée à l’autoconsommation', 'type': 'Suivi', 'unite': '%', 'frequence': 'Saisonnière', 'formule': '(Volume pour autoconsommation / Volume total produit) × 100'},

            # III. IDENTIFICATION & DIGITALISATION
            {'code': 'A11', 'libelle': '% de parcelles digitalisées (SIG)', 'type': 'Suivi', 'unite': '%', 'frequence': 'Trimestrielle', 'formule': '(Parcelles digitalisées / Parcelles totales) × 100'},
            {'code': 'A12', 'libelle': 'Nb d’exploitants enregistrés (ID unique)', 'type': 'Suivi', 'unite': 'Nombre', 'frequence': 'Trimestrielle', 'formule': 'Comptage exploitants enregistrés'},
            {'code': 'A13', 'libelle': 'Taux de couverture du registre des exploitants', 'type': 'Performance', 'unite': '%', 'frequence': 'Annuelle', 'formule': '(Exploitants enregistrés / Exploitants estimés) × 100'},
            {'code': 'A14', 'libelle': 'Taux d’exploitants identifiés', 'type': 'Suivi', 'unite': '%', 'frequence': 'Semestrielle', 'formule': '(Exploitants identifiés / Total exploitants) × 100'},

            # IV. FONCIER & CERTIFICATION
            {'code': 'A15', 'libelle': '% de parcelles sécurisées', 'type': 'Suivi', 'unite': '%', 'frequence': 'Annuelle', 'formule': '(Parcelles avec certificat / Total parcelles) × 100'},
            {'code': 'A16', 'libelle': '% d’exploitants bénéficiant d’un titre foncier', 'type': 'Suivi', 'unite': '%', 'frequence': 'Annuelle', 'formule': '(Exploitants avec certificat / Total exploitants) × 100'},
            {'code': 'A17', 'libelle': 'Nombre de conflits fonciers déclarés', 'type': 'Suivi', 'unite': 'Nombre', 'frequence': 'Semestrielle', 'formule': 'Comptage conflits signalés sur parcelles agricoles'},
            {'code': 'A18', 'libelle': 'Impact de la certification sur la production', 'type': 'Performance', 'unite': '%', 'frequence': 'Annuelle', 'formule': '(Rendement certifiées - Rendement non certifiées) / non certifiées × 100'},
            {'code': 'A19', 'libelle': 'Taux d’adoption de programmes fonciers', 'type': 'Performance', 'unite': '%', 'frequence': 'Annuelle', 'formule': '(Exploitants participant / Total exploitants) × 100'},

            # V. INTRANTS
            {'code': 'A20', 'libelle': 'Quantité d’engrais utilisée par ha', 'type': 'Suivi', 'unite': 'kg/ha', 'frequence': 'Saisonnière', 'formule': '∑ kg engrais / Surface cultivée (ha)'},
            {'code': 'A21', 'libelle': 'Prix moyen d’achat des intrants', 'type': 'Suivi', 'unite': 'MAD/kg', 'frequence': 'Mensuelle', 'formule': '∑ (Prix × Quantité) / Quantité totale'},
            {'code': 'A22', 'libelle': 'Taux d’accès aux intrants certifiés', 'type': 'Performance', 'unite': '%', 'frequence': 'Saisonnière', 'formule': '(Exploitants utilisant certifiés / Total exploitants) × 100'},
            {'code': 'A23', 'libelle': 'Volume d’intrants distribués', 'type': 'Suivi', 'unite': 'Tonnes', 'frequence': 'Trimestrielle', 'formule': 'Somme des quantités déclarées par filière'},
            {'code': 'A24', 'libelle': 'Coût moyen des intrants', 'type': 'Suivi', 'unite': 'MAD/unité', 'frequence': 'Mensuelle', 'formule': 'Σ (Quantité × Prix) / Quantité totale'},
            {'code': 'A25', 'libelle': 'Subvention intrants par exploitant', 'type': 'Performance', 'unite': 'MAD', 'frequence': 'Annuelle', 'formule': 'Subventions totales / Nb exploitants'},

            # VI. PRODUCTION
            {'code': 'A26', 'libelle': 'Superficie emblavée par filière', 'type': 'Suivi', 'unite': 'ha', 'frequence': 'Saisonnière', 'formule': 'Surface cultivée par filière'},
            {'code': 'A27', 'libelle': 'Rendement moyen par culture', 'type': 'Performance', 'unite': 'q/ha', 'frequence': 'Saisonnière', 'formule': 'Production récoltée / Surface récoltée'},
            {'code': 'A28', 'libelle': 'Utilisation moyenne des intrants', 'type': 'Suivi', 'unite': 'kg/ha', 'frequence': 'Campagne', 'formule': 'Quantité d’engrais/pesticide par hectare'},
            {'code': 'A29', 'libelle': 'Taux d’adoption de bonnes pratiques agricoles', 'type': 'Performance', 'unite': '%', 'frequence': 'Annuelle', 'formule': '(Exploitants normes GAP / Exploitants totaux) × 100'},
            {'code': 'A30', 'libelle': 'Taux d’adoption technologies (irrigation / digitalisation)', 'type': 'Performance', 'unite': '%', 'frequence': 'Annuelle', 'formule': '(Exploitants équipés / Total exploitants) × 100'},
            {'code': 'A31', 'libelle': 'Coût de production par unité', 'type': 'Performance', 'unite': 'MAD/kg', 'frequence': 'Campagne', 'formule': 'Dépenses totales / Production obtenue'},

            # VII. RÉCOLTE
            {'code': 'A32', 'libelle': 'Volume total récolté par filière', 'type': 'Suivi', 'unite': 'Tonnes', 'frequence': 'Campagne', 'formule': 'Σ Production par exploitant'},
            {'code': 'A33', 'libelle': 'Pertes post-récolte (%)', 'type': 'Performance', 'unite': '%', 'frequence': 'Campagne', 'formule': '(Volume perdu / Volume récolté) × 100'},
            {'code': 'A34', 'libelle': 'Qualité des produits récoltés', 'type': 'Performance', 'unite': '%', 'frequence': 'Campagne', 'formule': '(Volumes conformes / Volumes récoltés) × 100'},
            {'code': 'A35', 'libelle': 'Capacité de stockage installée / utilisée', 'type': 'Suivi', 'unite': 'T', 'frequence': 'Trimestrielle', 'formule': 'Volume stocké / Capacité totale'},

            # VIII. TRANSFORMATION
            {'code': 'A36', 'libelle': 'Nb unités de transformation connectées au SEAD', 'type': 'Suivi', 'unite': 'Nombre', 'frequence': 'Annuelle', 'formule': 'Comptage unités (coopératives, industries)'},
            {'code': 'A37', 'libelle': 'Valeur ajoutée brute par filière', 'type': 'Performance', 'unite': 'MAD', 'frequence': 'Annuelle', 'formule': '(Prix × Volume produit) – Intrants'},
            {'code': 'A38', 'libelle': 'Taux de produits certifiés / labellisés', 'type': 'Performance', 'unite': '%', 'frequence': 'Annuelle', 'formule': '(Volumes certifiés / Volumes commercialisés) × 100'},

            # IX. COMMERCIALISATION
            {'code': 'A39', 'libelle': 'Volume total commercialisé par marché', 'type': 'Suivi', 'unite': 'T', 'frequence': 'Mensuelle', 'formule': '∑ ventes locales, régionales, export'},
            {'code': 'A40', 'libelle': 'Prix moyen à la production par filière', 'type': 'Suivi', 'unite': 'MAD/kg', 'frequence': 'Hebdomadaire', 'formule': 'Moyenne pondérée prix par kg/litre'},
            {'code': 'A41', 'libelle': 'Part des exportations', 'type': 'Performance', 'unite': '%', 'frequence': 'Annuelle', 'formule': '(Volume exporté / Production totale) × 100'},
            {'code': 'A42', 'libelle': 'Revenu agricole moyen par exploitant', 'type': 'Performance', 'unite': 'MAD/an', 'frequence': 'Annuelle', 'formule': 'Σ Revenus / Nb exploitants'},
            {'code': 'A43', 'libelle': 'Taux d’accès aux marchés organisés', 'type': 'Performance', 'unite': '%', 'frequence': 'Semestrielle', 'formule': '(Exploitants intégrés / Total exploitants) × 100'},

            # X. SÉCURITÉ ALIMENTAIRE & IMPACTS
            {'code': 'A44', 'libelle': 'Score de Diversité Alimentaire des Ménages (SDAM)', 'type': 'Performance', 'unite': 'Index', 'frequence': 'Saisonnière', 'formule': 'Somme des groupes alimentaires consommés sur 24h / 7 jours'},
            {'code': 'A45', 'libelle': 'Score de Consommation Alimentaire (SCA)', 'type': 'Performance', 'unite': 'Index', 'frequence': 'Saisonnière', 'formule': 'Évaluation du niveau de consommation calorique'},
            {'code': 'A46', 'libelle': 'Nombre de repas par jour', 'type': 'Suivi', 'unite': 'Repas/jour', 'frequence': 'Saisonnière', 'formule': 'Moyenne des repas par ménage (saison normale et soudure)'},
            {'code': 'A47', 'libelle': 'Difficultés alimentaires', 'type': 'Suivi', 'unite': '%', 'frequence': 'Saisonnière', 'formule': '% de ménages déclarant manque alimentaire'},
            {'code': 'A48', 'libelle': 'Accès à l’eau potable et soins', 'type': 'Suivi', 'unite': '%', 'frequence': 'Annuelle', 'formule': '% de ménages avec accès eau/santé'},
            {'code': 'A49', 'libelle': 'Revenu agricole moyen par ménage', 'type': 'Performance', 'unite': 'MAD/ménage', 'frequence': 'Annuelle', 'formule': '(Revenus nets totaux / Nb ménages)'},
            {'code': 'A50', 'libelle': 'Contribution de la filière au PIB agricole', 'type': 'Performance', 'unite': '%', 'frequence': 'Annuelle', 'formule': '(VA filière / VA agricole) × 100'},
            {'code': 'A51', 'libelle': 'Taux de réduction de pauvreté rurale', 'type': 'Impact', 'unite': '%', 'frequence': 'Pluriannuel', 'formule': '(Pauvreté initiale – Pauvreté actuelle) / Pauvreté initiale'},
            {'code': 'A52', 'libelle': 'Couverture protection sociale', 'type': 'Performance', 'unite': '%', 'frequence': 'Annuelle', 'formule': '(Agriculteurs couverts / Total exploitants) × 100'},
            {'code': 'A53', 'libelle': 'Accès au financement', 'type': 'Performance', 'unite': '%', 'frequence': 'Annuelle', 'formule': 'Nb d’exploitants bénéficiant de crédits / Total'},
            {'code': 'A54', 'libelle': 'Taux de digitalisation des services agricoles', 'type': 'Performance', 'unite': '%', 'frequence': 'Annuelle', 'formule': '(Services digitalisés / Services totaux) × 100'},
            {'code': 'A55', 'libelle': 'Satisfaction des exploitants', 'type': 'Performance', 'unite': 'Index', 'frequence': 'Annuelle', 'formule': 'Score moyen d’enquête (1-5)'},
            {'code': 'A56', 'libelle': 'Suivi budgétaire programmes', 'type': 'Suivi / Performance', 'unite': '%', 'frequence': 'Annuelle', 'formule': 'Dépenses effectives / Budget voté × 100'},
        ]

        for item in indicators_data:
            obj, created = Indicateur.objects.get_or_create(
                code=item['code'],
                defaults={
                    'libelle': item['libelle'],
                    'unite': item['unite'],
                    'frequence': item['frequence'],
                    'formule_calcul': item['formule'],
                    'type': item['type'],
                }
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f"Indicateur {item['code']} créé."))
            else:
                # Mise à jour si déjà existant
                obj.libelle = item['libelle']
                obj.unite = item['unite']
                obj.frequence = item['frequence']
                obj.formule_calcul = item['formule']
                obj.type = item['type']
                obj.save()
                self.stdout.write(f"Indicateur {item['code']} mis à jour.")

        self.stdout.write(self.style.SUCCESS('--- Fin de l’initialisation des 56 indicateurs ---'))