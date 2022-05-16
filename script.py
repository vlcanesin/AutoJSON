from turtle import title
from bs4 import BeautifulSoup
import json

html = """
    <ul type="disc">
        <li>

            ARAÚJO, JANINE ; Menezes, Fabrício G. ; SILVA, HELOIZA F. O. ; VIEIRA, DAVI S. ; SILVA, SERGIO R. B. ; Bortoluzzi, Adailton J. ; SANT?ANNA, CELSO ; EUGENIO, MATEUS ; NERI, JANNYELY M. ; GASPAROTTO, LUIZ H. S. . Functionalization of gold nanoparticles with two aminoalcohol-based quinoxaline derivatives for targeting phosphoinositide 3-kinases (PI3KÎ±). <strong>NEW JOURNAL OF CHEMISTRY</strong>, v. 43, p. 1803-1811, 2019.
            <a href="http://dx.doi.org/10.1039/c8nj04314k"><strong>Cique aqui</strong></a>

        </li>
    </ul>
    <ul type="disc">
        <li>
            PESSOA, ALCIDÊNIO S. ; AGUIAR, GEAN PABLO S. ; VLADIMIR OLIVEIRA, J. ; Bortoluzzi, Adailton J. ; PAULINO, AMARILIS ; LANZA, MARCELO . Precipitation of resveratrol-isoniazid and resveratrol-nicotinamide cocrystals by gas antisolvent. <strong>JOURNAL OF SUPERCRITICAL FLUIDS,</strong> v. 145, p. 93-102, 2019.
            <a href="http://dx.doi.org/10.1016/j.supflu.2018.11.014"><strong>Cique aqui</strong></a>
        </li>
    </ul>
    <ul type="disc">
        <li>
            HEYING, RENATA S. ; DA SILVA, MARCOS PAULO ; WECKER, GIOVANA S. ; Peralta, Rosely A. ; Bortoluzzi, Adailton J. ; NEVES, Ademir . Unusual hydrolase-like activity of a mononuclear Fe(III) complex. <strong>INORGANIC CHEMISTRY COMMUNICATIONS</strong>, v. 102, p. 245-250, 2019.
            <a href="http://dx.doi.org/10.1016/j.inoche.2019.01.035"><strong>Cique aqui</strong></a>
        </li>
    </ul>
    <ul type="disc">
        <li>
            BECHER, TIAGO B. ; BRAGA, CAROLYNE B. ; BERTUZZI, DIEGO L. ; RAMOS, MIGUEL D. ; HASSAN, AYAZ ; CRESPILHO, FRANK N. ; Ornelas, Catia . The structure-property relationship in LAPONITE materials: from Wigner glasses to strong self-healing hydrogels formed by non-covalent interactions. <strong>Soft Matter,</strong> v. 15, p. 1278-1289, 2019.
            <a href="http://dx.doi.org/10.1039/c8sm01965g"><strong>Cique aqui</strong></a>
        </li>
    </ul>
    <ul type="disc">
        <li>
            BRAGA, CAROLYNE B. ; PERLI, GABRIEL ; BECHER, TIAGO B. ; Ornelas, Catia . Biodegradable and pH-Responsive Acetalated Dextran (Ac-Dex) Nanoparticles for NIR Imaging and Controlled Delivery of a Platinum-Based Prodrug into Cancer Cells. <strong>MOLECULAR PHARMACEUTICS,</strong> v. 16, p. 2083-2094, 2019.
            <a href="http://dx.doi.org/10.1021/acs.molpharmaceut.9b00058"><strong>Cique aqui</strong></a>
        </li>
    </ul>

    <ul type="disc">
        <li>
            Carlos, A. M. M. ; Stieler, R ; Lüdtke, D. S. . Catalytic Asymmetric Synthesis of 3-Aryl Phthalides.<strong> ORGANIC &amp; BIOMOLECULAR CHEMISTRY</strong>, v. 17, p. 283-289, 2019.
            <a href="http://dx.doi.org/10.1039/c8ob02872a"><strong>Clique aqui</strong></a>
        </li>
    </ul>
    <ul type="disc">
        <li>
            KFOURI, MARTA SIMÃO ; ANDRADE, MARIANA MARTINS REIS ; Sabadini, Edvaldo . Host-guest interaction into the cage of a supramolecular iron-organic complex - Is the process enthalpically or entropically- driven?. <strong>JOURNAL OF CHEMICAL THERMODYNAMICS</strong>, v. 131, p. 613-619, 2019.
            <a href="http://dx.doi.org/10.1016/j.jct.2018.12.020"><strong>Clique aqui</strong></a>
        </li>
    </ul>

    <ul type="disc">
        <li>
            DELOLO, FÁBIO G. ; OLIVEIRA, KELLEY C.B. ; DOS SANTOS, EDUARDO N. ; Gusevskaya, Elena V. . Hydroformylation of biomass-based hydroxyolefins in eco-friendly solvents: New fragrances from myrtenol and nopol.<strong> Molecular Catalysis,</strong> v. 462, p. 1-9, 2019.
            <a href="http://dx.doi.org/10.1016/j.mcat.2018.10.011"><strong>Clique aqui</strong></a>

        </li>
    </ul>
    <ul type="disc">
        <li>
            DE OLIVEIRA DIAS, ADELSON ; GUTIÉRREZ, MARÍA G.P. ; VILLARREAL, JESUS A.A. ; CARMO, RAUL L.L. ; OLIVEIRA, KELLEY C.B. ; SANTOS, ALEXANDRA G. ; DOS SANTOS, EDUARDO N. ; Gusevskaya, Elena V. . Sustainable route to biomass-based amines: rhodium catalyzed hydroaminomethylation in green solvents.<strong> APPLIED CATALYSIS A-GENERAL</strong>, v. 574, p. 97-104, 2019.
            <a href="http://dx.doi.org/10.1016/j.apcata.2019.02.003"><strong>Clique aqui</strong></a>

        </li>
    </ul>
    <ul type="disc">
        <li>
            DELOLO, FÁBIO G. ; DOS SANTOS, EDUARDO N. ; Gusevskaya, Elena V. . Anisole: a further step to sustainable hydroformylation. <strong>GREEN CHEMISTRY</strong>, v. 21, p. 1091-1098, 2019.
            <a href="http://dx.doi.org/10.1039/c8gc03750g"><strong>Clique aqui</strong></a>
        </li>
    </ul>
    <ul type="disc">
        <li>
            DE SOUZA, ÍVINA P. ; MACHADO, BÁRBARA DE P. ; DE CARVALHO, ALEXANDRE B. ; BINATTI, ILDEFONSO ; KRAMBROCK, KLAUS ; MOLPHY, ZARA ; KELLETT, ANDREW ; Pereira-Maia, Elene C. ; SILVA-CALDEIRA, PRISCILA P. . Exploring the DNA binding, oxidative cleavage, and cytotoxic properties of new ternary copper(II) compounds containing 4-aminoantipyrine and N,N-heterocyclic co-ligands. <strong>JOURNAL OF MOLECULAR STRUCTURE,</strong> v. 1178, p. 18-28, 2019.
            <a href="http://dx.doi.org/10.1016/j.molstruc.2018.10.004"><strong>Clique aqui</strong></a>

        </li>
    </ul>
    <ul type="disc">
        <li>
            OLIVEIRA, L. P. ; SOUZA, I. P. ; PAIXAO, D. A. ; SOUSA, L. M. ; LIMA, M. F. ; PEREIRA, C. S. ; Silva H ; Pereira-Maia, Elene C. ; GUERRA, W. . Pt(II) complexes of the type trans-[PtCl2(DMSO)(hydrazide)] and cis-[PtCl2(hydrazide)2]: Solvolysis and cytotoxic activity. <strong>JOURNAL OF MOLECULAR STRUCTURE,</strong> v. 1192, p. 76-81, 2019.
            <a href="http://dx.doi.org/10.1016/j.molstruc.2019.04.134"><strong>Clique aqui</strong></a>

        </li>
    </ul>

    <ul type="disc">
        <li>
            Machado, Fabricio . Modeling of the Penultimate Unit Effect in Chain-Growth Copolymerizations.<strong> International Journal of Polymer Science,</strong> v. 2019, p. 1-12, 2019.
            <a href="http://dx.doi.org/10.1155/2019/2912417"><strong>Clique aqui</strong></a>
        </li>
    </ul>
    <ul type="disc">
        <li>
            SCHULZ, MAYARA ; Gonzaga, Luciano Valdemiro ; DE SOUZA, VIVIANE ; FARINA, MARCELO ; Vitali, Luciano ; Micke, Gustavo Amadeu ; COSTA, Ana Carolina Oliveira ; Fett, Roseane . Neuroprotective effect of juçara (Euterpe edulis Martius) fruits extracts against glutamate-induced oxytosis in HT22 hippocampal cells.<strong> FOOD RESEARCH INTERNATIONAL</strong>, v. 01, p. 01-001, 2019.
            <a href="http://dx.doi.org/10.1016/j.foodres.2019.02.030"><strong>Clique aqui</strong></a>

        </li>
    </ul>
    <ul type="disc">
        <li>
            COSTA, THIAGO G. ; DA SILVA, BEATRIZ FELIX PIMENTA ; MATTOS, LUCAS PALMA ; SIEBERT, DIOGO ALEXANDRE ; Micke, Gustavo A. ; SZPOGANICZ, BRUNO ; MANGRICH, ANTÔNIO SALVIO . An original molecular approach to the use of clay minerals in the formulation of oil-based dyes and their sensitivity toward polar solvents - A case study. <strong>MICROCHEMICAL JOURNAL</strong>, v. 147, p. 142-149, 2019.
            <a href="http://dx.doi.org/10.1016/j.microc.2019.03.011"><strong>Clique aqui</strong></a>
            
        </li>
    </ul>
    <ul type="disc">
        <li>
            BRAGHINI, FRANCIELI ; BILUCA, FABÍOLA C. ; GONZAGA, LUCIANO V. ; KRACIK, ALINE S. ; VIEIRA, CLEIDE R. W. ; Vitali, Luciano ; Micke, Gustavo A. ; Costa, Ana C. O. ; Fett, Roseane . Impact of short-term thermal treatment on stingless bee honey ( Meliponinae) : Quality, phenolic compounds and antioxidant capacity. <strong>JOURNAL OF FOOD PROCESSING AND PRESERVATION</strong>, v. 01, p. e13954, 2019.
            <a href="http://dx.doi.org/10.1111/jfpp.13954"><strong>Clique aqui</strong></a>
            
        </li>
    </ul>
    <ul type="disc">
        <li>
            SIEBERT, DIOGO ALEXANDRE ; DE MELLO, FLÁVIA ; ALBERTON, MICHELE DEBIASI ; Vitali, Luciano ; Micke, Gustavo Amadeu . Determination of acetylcholinesterase and &#945;-glucosidase inhibition by electrophoretically-mediated microanalysis and phenolic profile by HPLC-ESI-MS/MS of fruit juices from Brazilian Myrtaceae Plinia cauliflora (Mart.) Kausel and Eugenia uniflora L.. <strong>NATURAL PRODUCT RESEARCH</strong>, v. 01, p. 1-6, 2019.
            <a href="http://dx.doi.org/10.1080/14786419.2018.1550760"><strong>Clique aqui</strong></a>
            
        </li>
    </ul>
    <ul type="disc">
        <li>
            COSTA, TANIA MARIA ; KAUFMANN, VANDER ; PAGANELLI, CAMILA JERIANE ; SIEBERT, DIOGO ALEXANDRE ; Micke, Gustavo Amadeu ; ALBERTON, MICHELE DEBIASI ; TAVARES, LORENA BENATHAR BALLOD ; DE OLIVEIRA, DÉBORA . Kinetic identification of phenolic compounds and potential production of caffeic acid by Ganoderma lipsiense in solid-state fermentation. <strong>BIOPROCESS AND BIOSYSTEMS ENGINEERING,</strong> v. 01, p. 001, 2019.
            <a href="http://dx.doi.org/10.1007/s00449-019-02131-8"><strong>Clique aqui</strong></a>
            
        </li>
    </ul>
    <ul type="disc">
        <li>
            HOCHHEIM, SABRINA ; GUEDES, ALESSANDRO ; FACCIN-GALHARDI, LIGIA ; RECHENCHOSKI, DANIELE ZENDRINI ; NOZAWA, CARLOS ; LINHARES, ROSA ELISA ; FILHO, HERCÍLIO HIGINO DA SILVA ; RAU, MARTINHO ; SIEBERT, DIOGO ALEXANDRE ; MICKE, GUSTAVO ; CORDOVA, CAIO MAURICIO MENDES DE . Determination of phenolic profile by HPLC-ESI-MS/MS, antioxidant activity, in vitro cytotoxicity and anti-herpetic activity of propolis from the Brazilian native bee Melipona quadrifasciata.<strong> Revista Brasileira de Farmacognosia-Brazilian Journal of Pharmacognosy</strong>, v. 01, p. 001, 2019.
            <a href="http://dx.doi.org/10.1016/j.bjp.2018.12.010"><strong>Clique aqui</strong></a>
            
        </li>
    </ul>
    <ul type="disc">
        <li>
            FERNANDES, ALESSANDRA A. G. ; STIVANIN, MATEUS L. ; Jurberg, Igor D. . RuCl 3 / PPh 3 - Catalyzed Direct Conversion of Isoxazol-5-ones to 2,3-Disubstituted Pyridines.<strong> ChemistrySelect,</strong> v. 4, p. 3360-3365, 2019.
            <a href="http://dx.doi.org/10.1002/slct.201900761"><strong>Clique aqui</strong></a>

        </li>
    </ul>
    <ul type="disc">
        <li>
            FERNANDES, ALESSANDRA A. G. ; DA SILVA, AMANDA F. ; OKADA, CELSO Y. ; SUZUKAWA, VITOR ; CORMANICH, RODRIGO A. ; Jurberg, Igor D. . General Platform for the Conversion of Isoxazol-5-ones to 3,5-Disubstituted Isoxazoles via Nucleophilic Substitutions and Palladium Catalyzed Cross-Coupling Strategies.<strong> EUROPEAN JOURNAL OF ORGANIC CHEMISTRY,</strong> v. 2019, p. 3022-3034, 2019.
            <a href="http://dx.doi.org/10.1002/ejoc.201900187"><strong>Clique aqui</strong></a>
        </li>
    </ul>
    <ul type="disc">
        <li>
            MATIELLO, GABRIELA I. ; PAZINI, ALESSANDRA ; DA SILVA, KÁCRIS I.M. ; DA COSTA, RAFAELA G.M. ; EBELING, GÜNTER ; Dupont, Jairton ; LIMBERGER, JONES ; SCHOLTEN, JACKSON D. . Isothiouronium salts as useful and odorless intermediates for the synthesis of thiaalkylimidazolium ionic liquids.<strong> TETRAHEDRON LETTERS,</strong> v. 60, p. 780-784, 2019.
            <a href="http://dx.doi.org/10.1016/j.tetlet.2019.02.013"><strong>Clique aqui</strong></a>
        </li>
    </ul>
    <ul type="disc">
        <li>
            SOUZA, JOSÉ D. ; SOUZA, VIRGÍNIA S. ; SCHOLTEN, JACKSON D. . Synthesis of Hybrid Zinc-Based Materials from Ionic Liquids: A Novel Route to Prepare Active Zn Catalysts for the Photoactivation of Water and Methane.<strong> ACS Sustainable Chemistry &amp; Engineering,</strong> v. 7, p. 8090-8098, 2019.
            <a href="http://dx.doi.org/10.1021/acssuschemeng.8b04809"><strong>Clique aqui</strong></a>

        </li>
    </ul>
    <ul type="disc">
        <li>
            QADIR, MUHAMMAD I. ; BERNARDI, FABIANO ; SCHOLTEN, JACKSON D. ; BAPTISTA, DANIEL L. ; Dupont, Jairton . Synergistic CO2 hydrogenation over bimetallic Ru/Ni nanoparticles in ionic liquids.<strong> APPLIED CATALYSIS B-ENVIRONMENTAL,</strong> v. 252, p. 10-17, 2019.
            <a href="http://dx.doi.org/10.1016/j.apcatb.2019.04.005"><strong>Clique aqui</strong></a>
        </li>
    </ul>
    <ul type="disc">
        <li>
            LIMA, MARCELO F. ; DA CRUZ, PRISCILLA AMANDA URBANO ; FERNANDES, MARIA EDUARDA CAMILO ; POLAQUINI, CARLOS ; MIGUEL, ELIZABETH L. M. ; Pliego, Josefredo R. ; SCORSIN, LEANDRO ; OLIVEIRA, BRUNO SURDI ; NOME, Faruk . Cleaving paraoxon with hydroxylamine: Ammonium oxide isomer favors a Frontside attack mechanism. <strong>JOURNAL OF PHYSICAL ORGANIC CHEMISTRY,</strong> v. 32, p. e3866, 2019.
            <a href="http://dx.doi.org/10.1002/poc.3866"><strong>Clique aqui</strong></a>
        </li>
    </ul>
    <ul type="disc">
        <li>
            NOGUEIRA, I. C. ; PLIEGO, J. R. . Counter-ion and solvent effects in the C- and O-alkylation of the phenoxide ion with allyl chloride.<strong> JOURNAL OF PHYSICAL ORGANIC CHEMISTRY,</strong> v. 32, p. e3947, 2019.
            <a href="http://dx.doi.org/10.1002/poc.3947"><strong>Clique aqui</strong></a>
        </li>
    </ul>

    <ul type="disc">
        <li>
            BELTRAO-NUNES, ANA-PAOLA ; SENNOUR, RADIA ; ARUS, VASILICA-ALISA ; ANOMA, SARAH ; Pires, MarÃ§al ; BOUAZIZI, NABIL ; ROY, RENÉ ; AZZOUZ, ABDELKRIM . CO2 capture by coal ash-derived zeolites- roles of the intrinsic basicity and hydrophilic character.<strong> JOURNAL OF ALLOYS AND COMPOUNDS</strong>, v. 778, p. 866-877, 2019.
            <a href="http://dx.doi.org/10.1016/j.jallcom.2018.11.133"><strong>Clique aqui</strong></a>
        </li>
    </ul>
    <ul type="disc">
        <li>
            Fallavena, Vera L. V. ; Pires, Marçal José Rodrigues ; FERRARINI, S. F. ; SILVEIRA, A. P. B. . Evaluation of Zeolite/Backfill Blend for Acid Mine Drainage Remediation in Coal Mine.<strong> ENERGY &amp; FUELS,</strong> v. 32, p. 2019-2027, 2018.
            <a href="http://dx.doi.org/10.1021/acs.energyfuels.7b03322"><strong>Clique aqui</strong></a>
        </li>
    </ul>
    <ul type="disc">
        <li>
            DOS SANTOS NASCIMENTO, MARCUS VINICIUS PEREIRA ; MATTAR MUNHOZ, ANTONIO CARLOS ; DE CAMPOS FACCHIN, ANTONIO BRUNO MATHEUS ; FRATONI, EDUARDA ; ROSSA, THAÍS ANDREIA ; MANDOLESI SÁ, MARCUS ; CAMPA, CARLO COSIMO ; CIRAOLO, ELISA ; HIRSCH, EMILIO ; DALMARCO, EDUARDO MONGUILHOTT . New pre-clinical evidence of anti-inflammatory effect and safety of a substituted fluorophenyl imidazole. <strong>BIOMEDICINE &amp; PHARMACOTHERAPY</strong>, v. 111, p. 1399-1407, 2019.
            <a href="http://dx.doi.org/10.1016/j.biopha.2019.01.052"><strong>Clique aqui</strong></a>
        </li>
    </ul>
    <ul type="disc">
        <li>
            ECHEMENDÍA, RADELL ; DA SILVA, GUSTAVO P. ; KAWAMURA, MEIRE Y. ; DE LA TORRE, ALEXANDER F. ; Corrêa, Arlene G. ; FERREIRA, MARCO A. B. ; Rivera, Daniel G. ; Paixão, Márcio W. . A stereoselective sequential organocascade and multicomponent approach for the preparation of tetrahydropyridines and chimeric derivatives. <strong>CHEMICAL COMMUNICATIONS (LONDON. 1996. ONLINE)</strong>, v. 55, p. 286-289, 2019.
            <a href="http://dx.doi.org/10.1039/C8CC06871B"><strong>Clique aqui</strong></a>
        </li>
    </ul>
    <ul type="disc">
        <li>
            DA SILVA, ALLAN ; DOS SANTOS, DEBORAH ; PAIXÃO, MARCIO ; Corrê;a, Arlene . Stereoselective Multicomponent Reactions in the Synthesis or Transformations of Epoxides and Aziridines. <strong>MOLECULES</strong>, v. 24, p. 630, 2019.
            <a href="http://dx.doi.org/10.3390/molecules24030630"><strong>Clique aqui</strong></a>
        </li>
    </ul>
    <ul type="disc">
        <li>
            CORREA, ARLENE ; DANTAS, JULIANA ARANTES ; CORREIA, JOSÉ TIAGO MENEZES ; PAIXÃO, MARCIO WEBER . Photochemistry of carbonyl compounds: application on metal-free reactions.<strong> ChemPhotoChem</strong>, v. 3, p. 00-00, 2019.
            <a href="http://dx.doi.org/10.1002/cptc.201900044"><strong>Clique aqui</strong></a>
        </li>
    </ul>
    <ul type="disc">
        <li>
            FERREIRA, JORGE ; ZILZ, RAQUEL ; BOEIRA, IGOR S. ; DA SILVA, SABRINA M. ; CASAGRANDE, ADRIANA C.A. ; Casagrande, Osvaldo L. . Chromium complexes based on thiophene-imine ligands for ethylene oligomerization.<strong> APPLIED ORGANOMETALLIC CHEMISTRY,</strong> v. 33, p. e4697, 2019.
            <a href="http://dx.doi.org/10.1002/aoc.4697"><strong>Clique aqui</strong></a>
        </li>
    </ul>
    <ul type="disc">
        <li>
            JUNGES, C.H. ; DRESCH, L.C. ; COSTA, M.T. ; TIRLONI, B. ; CASAGRANDE, O.L. ; STIELER, R. . Pyrazolyl-phosphinoyl nickel (II) complexes: synthesis, characterization and ethylene dimerization studies.<strong> APPLIED ORGANOMETALLIC CHEMISTRY,</strong> v. 33, p. e4887, 2019.
            <a href="http://dx.doi.org/10.1002/aoc.4887"><strong>Clique aqui</strong></a>
        </li>
    </ul>

    <ul type="disc">
        <li>
            BRONDANI, PATRÍCIA BULEGON ; MITTERSTEINER, MATEUS ; Voigt, M. A. ; klinkowski, B. H. ; SCHARF, DILAMARA ; DE JESUS, PAULO CESAR . Synthetic Versatility of Lipases: Application for Si-O Bond Formation and Cleavage. <strong>SYNTHESIS-STUTTGART</strong>, v. 51, p. 477-485, 2019.
            <a href="http://dx.doi.org/10.1055/s-0037-1610281"><strong>Clique aqui</strong></a>
        </li>
    </ul>
    <ul type="disc">
        <li>
            SENS DA SILVA, RODRIGO ; VINÍCIUS PEDROSO, ANDRÉ ; CESAR DE JESUS, PAULO ; LAFAYETTE NEVES GELINSKI, JANE MARY ; MARCEL BORGES, ENDLER . Quantitation of Vitamin C in Supplements Using Titrimetric, Molecular Absorption Spectroscopy and Digital Imagens. <strong>REVISTA VIRTUAL DE QUÍMICA,</strong> v. 11, p. 155-179, 2019.
            <a href="http://dx.doi.org/10.21577/1984-6835.20190012"><strong>Clique aqui</strong></a>
        </li>
    </ul>
    <ul type="disc">
        <li>
            Schneider, Paulo Henrique; COELHO, FELIPE L. ; Gonçalves, Paulo F. B. ; CAMPO, LEANDRA F. ; GIL, EDUARDA S. . Intramolecular hydroamination of selenoalkynes to 2-selenylindole in absence of catalyst.<strong> CHEMISTRY-A EUROPEAN JOURNAL, </strong>v. v, p. chem.201901667, 2019.
            <a href="http://dx.doi.org/10.1002/chem.201901667"><strong>Clique aqui</strong></a>
        </li>
    </ul>
    <ul type="disc">
        <li>
            DE SALLES, HELENA ; DA SILVA, TIAGO ; RADATZ, CÁTIA ; AFFELDT, RICARDO ; BENVENUTTI, EDILSON ; SCHNEIDER, PAULO . Imidazo[1,2-a]pyridine A3-Coupling Catalyzed by a Cu/SiO2 Material.<strong> JOURNAL OF THE BRAZILIAN CHEMICAL SOCIETY,</strong> v. 00, p. 00, 2019.
            <a href="http://dx.doi.org/10.21577/0103-5053.20190089"><strong>Clique aqui</strong></a>
        </li>
    </ul>
    <ul type="disc">
        <li>
            RAMPON, DANIEL ; LIMA, DAVID BORBA ; LUZ, EDUARDO Q. ; BALAGUEZ, RENATA ; Schneider, Paulo Henrique ; Alves, Diego . Transition Metal Catalysed Direct Selanylation of Arenes and Heteroarenes. <strong>DALTON TRANSACTIONS</strong>, v. 00, p. 00, 2019.
            <a href="http://dx.doi.org/10.1039/c9dt00473d"><strong>Clique aqui</strong></a>
        </li>
    </ul>
    <ul type="disc">
        <li>
            RODRIGUES, THENNER S. ; DE MOURA, ARTHUR B.L. ; E SILVA, FELIPE A. ; CANDIDO, EDUARDO G. ; DA SILVA, ANDERSON G.M. ; DE OLIVEIRA, DANIELA C. ; QUIROZ, JHON ; Camargo, Pedro H.C. ; BERGAMASCHI, VANDERLEI S. ; FERREIRA, JOÃO C. ; LINARDI, MARCELO ; FONSECA, FABIO C. . Ni supported Ce0.9Sm0.1O2-&#948; nanowires: An efficient catalyst for ethanol steam reforming for hydrogen production.<strong> FUEL,</strong> v. 237, p. 1244-1253, 2019.
            <a href="http://dx.doi.org/10.1016/j.fuel.2018.10.053"><strong>Clique aqui</strong></a>
        </li>
    </ul>
    <ul type="disc">
        <li>
            PINHEIRO, VICTOR S. ; PAZ, EDSON C. ; AVEIRO, LUCI R. ; PARREIRA, LUANNA S. ; SOUZA, FELIPE M. ; Camargo, Pedro H.C. ; SANTOS, MAURO C. . Mineralization of paracetamol using a gas diffusion electrode modified with ceria high aspect ratio nanostructures. <strong>ELECTROCHIMICA ACTA,</strong> v. 295, p. 39-49, 2019.
            <a href="http://dx.doi.org/10.1016/j.electacta.2018.10.097"><strong>Clique aqui</strong></a>
        </li>
    </ul>
    <ul type="disc">
        <li>
            GUALTEROS, JESUS A. D. ; GARCIA, MARCO A. S. ; DA SILVA, ANDERSON G. M. ; RODRIGUES, THENNER S. ; CÂNDIDO, EDUARDO G. ; E SILVA, FELIPE A. ; FONSECA, FABIO C. ; QUIROZ, JHON ; DE OLIVEIRA, DANIELA C. ; DE TORRESI, SUSANA I. CÓRDOBA ; DE MOURA, CARLA V. R. ; Camargo, Pedro H. C. ; DE MOURA, EDMILSON M. . Synthesis of highly dispersed gold nanoparticles on Al2O3, SiO2, and TiO2 for the solvent-free oxidation of benzyl alcohol under low metal loadings.<strong> JOURNAL OF MATERIALS SCIENCE,</strong> v. 54, p. 238-251, 2019.
            <a href="http://dx.doi.org/10.1007/s10853-018-2827-x"><strong>Clique aqui</strong></a>
        </li>
    </ul>
    <ul type="disc">
        <li>
            ZHU, KAI ; WANG, CHUNRUI ; Camargo, Pedro H. C. ; WANG, JIALE . Investigating the effect of MnO band gap in hybrid MnO -Au materials over the SPR-mediated activities under visible light.<strong> Journal of Materials Chemistry A,</strong> v. 7, p. 925-931, 2019.
            <a href="http://dx.doi.org/10.1039/C8TA09785B"><strong>Clique aqui</strong></a>
        </li>
    </ul>
    <ul type="disc">
        <li>
            DE SOUZA, PRISCILLA ; SILVESTER, LISHIL ; DA SILVA, ANDERSON ; FERNANDES, CIBELE ; RODRIGUES, THENNER ; PAUL, SEBASTIEN ; CAMARGO, PEDRO ; WOJCIESZAK, ROBERT . Exploiting the Synergetic Behavior of PtPd Bimetallic Catalysts in the Selective Hydrogenation of Glucose and Furfural.<strong> Catalysts,</strong> v. 9, p. 132, 2019.
            <a href="http://dx.doi.org/10.3390/catal9020132"><strong>Clique aqui</strong></a>
        </li>
    </ul>
    <ul type="disc">
        <li>
            OLIVEIRA, LINCOLN P. ; DE A. MONTENEGRO, MATEUS ; LIMA, FRANCISCO C.A. ; Suarez, Paulo A.Z. ; DA SILVA, EID CAVALCANTE ; Meneghetti, Mario R. ; Meneghetti, Simoni M.P. . Biofuel production from Pachira aquatic Aubl and Magonia pubescens A St-Hil: Physical-chemical properties of neat vegetable oils, methyl-esters and bio-oils (hydrocarbons).<strong> INDUSTRIAL CROPS AND PRODUCTS,</strong> v. 127, p. 158-163, 2019.
            <a href="http://dx.doi.org/10.1016/j.indcrop.2018.10.061"><strong>Clique aqui</strong></a>
        </li>
    </ul>
    <ul type="disc">
        <li>
            SILVA, LAURA L. ; ALKIMIM, ISABELLA P. ; COSTA, JHOSIANNA P.V.S. ; Meneghetti, Simoni M.P. ; CARDOSO, DILSON . Catalytic evaluation of MCM-41 hybrid silicas in the transesterification reactions.<strong> MICROPOROUS AND MESOPOROUS MATERIALS,</strong> v. 284, p. 265-275, 2019.
            <a href="http://dx.doi.org/10.1016/j.micromeso.2019.04.024"><strong>Clique aqui</strong></a>
        </li>
    </ul>
    <ul type="disc">
        <li>
            SAUER, ANDRÉ C. ; WOLF, LUCAS ; QUOOS, NATÁLIA ; RODRIGUES, MARIELE B. ; BRAGA, ANTÔNIO L. ; RODRIGUES, Oscar E. D. ; Dornelles, Luciano . A Straightforward and High-Yielding Synthesis of 1,2,4-Oxadiazoles from Chiral N -Protected &#945; -Amino Acids and Amidoximes in Acetone-Water: An Eco-Friendly Approach.<strong> Journal of Chemistry,</strong> v. 2019, p. 1-9, 2019.
            <a href="http://dx.doi.org/10.1155/2019/8589325"><strong>Clique aqui</strong></a>
        </li>
    </ul>
    <ul type="disc">
        <li>
            AMORIM, ANDRÉ L. ; PETERLE, MARCOS M. ; GUERREIRO, ANA ; COIMBRA, DANIEL F. ; HEYING, RENATA S. ; CARAMORI, GIOVANI F. ; Braga, Antonio L. ; BORTOLUZZI, ADAILTON J. ; NEVES, ADEMIR ; BERNARDES, GONÇALO J. L. ; PERALTA, ROSELY A. . Synthesis, characterization and biological evaluation of new manganese metal carbonyl compounds that contain sulfur and selenium ligands as a promising new class of CORMs.<strong> DALTON TRANSACTIONS</strong>, v. 48, p. 5574-5584, 2019.
            <a href="http://dx.doi.org/10.1039/c9dt00616h"><strong>Clique aqui</strong></a>
        </li>
    </ul>

    <ul type="disc">
        <li>
            DELOLO, FÁBIO G. ; OLIVEIRA, KELLEY C.B. ; DOS SANTOS, EDUARDO N. ; Gusevskaya, Elena V. . Hydroformylation of biomass-based hydroxyolefins in eco-friendly solvents: New fragrances from myrtenol and nopol. <strong>Molecular Catalysis,</strong> v. 462, p. 1-9, 2019.
            <a href="http://dx.doi.org/10.1016/j.mcat.2018.10.011"><strong>Clique aqui</strong></a>
        </li>
    </ul>
    <ul type="disc">
        <li>
            DE OLIVEIRA DIAS, ADELSON ; GUTIÉRREZ, MARÍA G.P. ; VILLARREAL, JESUS A.A. ; CARMO, RAUL L.L. ; OLIVEIRA, KELLEY C.B. ; SANTOS, ALEXANDRA G. ; DOS SANTOS, EDUARDO N. ; Gusevskaya, Elena V. . Sustainable route to biomass-based amines: rhodium catalyzed hydroaminomethylation in green solvents.<strong> APPLIED CATALYSIS A-GENERAL</strong>, v. 574, p. 97-104, 2019.
            <a href="http://dx.doi.org/10.1016/j.apcata.2019.02.003"><strong>Clique aqui</strong></a>
        </li>
    </ul>
    <ul type="disc">
        <li>
            DELOLO, FÁBIO G. ; DOS SANTOS, EDUARDO N. ; Gusevskaya, Elena V. . Anisole: a further step to sustainable hydroformylation. <strong>GREEN CHEMISTRY</strong>, v. 21, p. 1091-1098, 2019.
            <a href="http://dx.doi.org/10.1039/c8gc03750g"><strong>Clique aqui</strong></a>
        </li>
    </ul>

    <ul type="disc">
        <li>
            QADIR, MUHAMMAD I. ; ZANATTA, MARCILEIA ; GIL, EDUARDA S. ; STASSEN, HUBERT K. ; GONÃ‡ALVES, PAULO ; NETO, BRENNO A. D. ; DE'SOUZA, PAULO E. N. ; Dupont, Jairton . Photocatalytic Reverse Semi-Combustion Driven by Ionic Liquids.<strong> ChemSusChem,</strong> v. 7, p. 1011-1016, 2019.
            <a href="http://dx.doi.org/10.1002/cssc.201802974"><strong>Clique aqui</strong></a>
        </li>
    </ul>
    <ul type="disc">
        <li>
            LOGUERCIO, LARA FERNANDES ; DE MATOS, CAROLINA FERREIRA ; DE OLIVEIRA, MATHEUS COSTA ; MARIN, GRACIANE ; KHAN, SHERDIL ; Dupont, Jairton ; TEIXEIRA, SERGIO RIBEIRO ; BALZARETTI, NAIRA M. ; SANTOS, JACQUELINE F. LEITE ; SANTOS, MARCOS J. LEITE . Polypyrrole/Ionic Liquid/Au Nanoparticle Counter-Electrodes for Dye-Sensitized Solar Cells: Improving Charge-Transfer Resistance at the CE/Electrolyte Interface.<strong> JOURNAL OF THE ELECTROCHEMICAL SOCIETY,</strong> v. 166, p. H3188-H3194, 2019.
            <a href="http://dx.doi.org/10.1149/2.0271905jes"><strong>Clique aqui</strong></a>
        </li>
    </ul>
    <ul type="disc">
        <li>
            LEU, MEIKE K. ; VICENTE, ISABEL ; FERNANDES, JESUM ALVES ; DE PEDRO, IMANOL ; Dupont, Jairton ; SANS, VICTOR ; LICENCE, PETER ; GUAL, AITOR ; CANO, ISRAEL . On the real catalytically active species for CO2 fixation into cyclic carbonates under near ambient conditions: Dissociation equilibrium of [BMIm][Fe(NO)2Cl2] dependant on reaction temperature. <strong>APPLIED CATALYSIS B-ENVIRONMENTAL,</strong> v. 245, p. 240-250, 2019.
            <a href="http://dx.doi.org/10.1016/j.apcatb.2018.12.062"><strong>Clique aqui</strong></a>
        </li>
    </ul>
    <ul type="disc">
        <li>
            ZANATTA, MARCILEIA ; SIMON, NATHALIA M. ; DOS'SANTOS, FRANCISCO P. ; CORVO, MARTA C. ; CABRITA, EURICO J. ; Dupont, Jairton . Correspondence on Preorganization and Cooperation for Highly Efficient and Reversible Capture of Low-Concentration CO 2 by Ionic Liquids. <strong>ANGEWANDTE CHEMIE-INTERNATIONAL EDITION,</strong> v. 58, p. 382-385, 2019.
            <a href="http://dx.doi.org/10.1002/anie.201712252"><strong>Clique aqui</strong></a>
        </li>
    </ul>
    <ul type="disc">
        <li>
            KIBLER, ALEXANDER J. ; MARTÍN, CARMEN ; CAMERON, JAMIE M. ; ROGALSKA, AGATA ; Dupont, Jairton ; WALSH, DARREN A. ; NEWTON, GRAHAM N. . Physical and Electrochemical Modulation of Polyoxometalate Ionic Liquids via Organic Functionalization. <strong>EUROPEAN JOURNAL OF INORGANIC CHEMISTRY</strong>, v. 2019, p. 456-460, 2019.
            <a href="http://dx.doi.org/10.1002/ejic.201800578"><strong>Clique aqui</strong></a>
        </li>
    </ul>
    <ul type="disc">
        <li>
            ZANATTA, MARCILEIA ; ANTUNES, VÍCTOR U. ; TORMENA, CÁUDIO F. ; Dupont, Jairton ; DOS SANTOS, FRANCISCO P. . Dealing with supramolecular structure for ionic liquids: a DOSY NMR approach. <strong>PHYSICAL CHEMISTRY CHEMICAL PHYSICS,</strong> v. 21, p. 2567-2571, 2019.
            <a href="http://dx.doi.org/10.1039/c8cp07071g"><strong>Clique aqui</strong></a>
        </li>
    </ul>
    <ul type="disc">
        <li>
            Dupont, Jairton . Hydrogen: The Mother Atom. <strong>CHEMISTRY-A EUROPEAN JOURNAL</strong>, v. 25, p. 3404-3404, 2019.
            <a href="http://dx.doi.org/10.1002/chem.201803971"><strong>Clique aqui</strong></a>
        </li>
    </ul>
    <ul type="disc">
        <li>
            MATIELLO, GABRIELA I. ; PAZINI, ALESSANDRA ; DA SILVA, KÁCRIS I.M. ; DA COSTA, RAFAELA G.M. ; Ebeling, Günter ; Dupont, Jairton ; LIMBERGER, JONES ; Scholten, Jackson D. . Isothiouronium salts as useful and odorless intermediates for the synthesis of thiaalkylimidazolium ionic liquids. <strong>TETRAHEDRON LETTERS</strong>, v. 60, p. 780-784, 2019.
            <a href="http://dx.doi.org/10.1016/j.tetlet.2019.02.013"><strong>Clique aqui</strong></a>
        </li>
    </ul>
    <ul type="disc">
        <li>
            FAGGION, DEONILDO ; GONÇALVES, WELLINGTON D. G. ; Dupont, Jairton . CO2 Electroreduction in Ionic Liquids. <strong>Frontiers in Chemistry</strong>, v. 7, p. 102, 2019.
            <a href="http://dx.doi.org/10.3389/fchem.2019.00102"><strong>Clique aqui</strong></a>
        </li>
    </ul>
    <ul type="disc">
        <li>
            QADIR, MUHAMMAD I. ; BERNARDI, FABIANO ; Scholten, Jackson D. ; BAPTISTA, DANIEL L. ; Dupont, Jairton . Synergistic CO2 Hydrogenation over Bimetallic Ru/Ni Nanoparticles in Ionic Liquids. <strong>APPLIED CATALYSIS B-ENVIRONMENTAL,</strong> v. 252, p. 10-17, 2019.
            <a href="http://dx.doi.org/10.1016/j.apcatb.2019.04.005"><strong>Clique aqui</strong></a>
        </li>
    </ul>
    <ul type="disc">
        <li>
            RAVISHANKAR, T.N. ; DE O. VAZ, M. ; RAMAKRISHNAPPA, T. ; TEIXEIRA, S.R. ; DUPONT, J. . Ionic liquid-assisted hydrothermal synthesis of Nb/TiO2 nanocomposites for efficient photocatalytic hydrogen production and photodecolorization of Rhodamine B under UV-visible and visible light illuminations. <strong>Materials Today Chemistry,</strong> v. 12, p. 373-385, 2019.
            <a href="http://dx.doi.org/10.1016/j.mtchem.2019.04.001"><strong>Clique aqui</strong></a>
        </li>
    </ul>
    <ul type="disc">
        <li>
            OLIVEIRA, LINCOLN P. ; DE A. MONTENEGRO, MATEUS ; LIMA, FRANCISCO C.A. ; SUAREZ, PAULO A.Z. ; DA SILVA, EID CAVALCANTE ; MENEGHETTI, MARIO R. ; MENEGHETTI, SIMONI M.P. . Biofuel production from Pachira aquatic Aubl and Magonia pubescens A St-Hil: Physical-chemical properties of neat vegetable oils, methyl-esters and bio-oils (hydrocarbons). <strong>INDUSTRIAL CROPS AND PRODUCTS,</strong> v. 127, p. 158-163, 2019.
            <a href="http://dx.doi.org/10.1016/j.indcrop.2018.10.061"><strong>Clique aqui</strong></a>
        </li>
    </ul>
    <ul type="disc">
        <li>
            COSTA, KÊNIA DE P. ; DE VIVEIROS, BÁRBARA M. ; SCHMIDT JUNIOR, MARCO AURELIO S. ; Suarez, Paulo A.Z. ; REZENDE, MICHELLE J.C. . Chemical transformations in technical cashew nut shell liquid and isolated mixture of cardanols, evaluation of the antioxidant activity and thermal stability of the products for use in pure biodiesel.<strong> FUEL,</strong> v. 235, p. 1010-1018, 2019.
            <a href="http://dx.doi.org/10.1016/j.fuel.2018.08.111"><strong>Clique aqui</strong></a>
        </li>
    </ul>
    <ul type="disc">
        <li>
            OLIVEIRA, LINCOLN P. ; DE A. MONTENEGRO, MATEUS ; LIMA, FRANCISCO C.A. ; Suarez, Paulo A.Z. ; DA SILVA, EID CAVALCANTE ; Meneghetti, Mario R. ; MENEGHETTI, SIMONI M.P. . Biofuel production from Pachira aquatic Aubl and Magonia pubescens A St-Hil: Physical-chemical properties of neat vegetable oils, methyl-esters and bio-oils (hydrocarbons).<strong> INDUSTRIAL CROPS AND PRODUCTS</strong>, v. 127, p. 158-163, 2019.
            <a href="http://dx.doi.org/10.1016/j.indcrop.2018.10.061"><strong>Clique aqui</strong></a>

        </li>
    </ul>

    <ul type="disc">
        <li>
            LIGIÉRO, CAROLINA ; DE OLIVEIRA, THIAGO VALDARES ; FONTES, CHÉRBEL ; BARRAGAN, JOSÉ THIAGO ; SO, FERNANDA ; KUBOTA, LAURO ; NOME, RENÉ ; MIRANDA, PAULO . TIMPZ: An exquisite building block for metal/hydrogen coordination polymers.<strong> EUROPEAN JOURNAL OF INORGANIC CHEMISTRY,</strong> v. 17, p. 2291, 2019.
            <a href="http://dx.doi.org/10.1002/ejic.201900229"><strong>Clique aqui</strong></a>
        </li>
    </ul>
    <ul type="disc">
        <li>
            RIBEIRO, IRIS R. ; IMMICH, MAIRA F. ; LUNDBERG, DAN ; POLETTO, FERNANDA ; Loh, Watson . Physiological neutral pH drives a gradual lamellar-to-reverse cubic-to-reverse hexagonal phase transition in phytantriol-based nanoparticles.<strong> COLLOIDS AND SURFACES B-BIOINTERFACES,</strong> v. x, p. y, 2019.
            <a href="http://dx.doi.org/10.1016/j.colsurfb.2019.01.055"><strong>Clique aqui</strong></a>
        </li>
    </ul>
    <ul type="disc">
        <li>
            OTONI, CAIO GOMIDE ; FIGUEIREDO, JULIANA ; CAPELETTI, LARISSA ; CARDOSO, MATEUS BORBA ; BERNARDES, JULIANA DA SILVA ; Loh, Watson . Tailoring the antimicrobial response of cationic nanocellulose-based foams through cryo-templating. <strong>ACS Applied Bio Materials</strong>, v. x, p. acsabm.9b00034, 2019.
            <a href="http://dx.doi.org/10.1021/acsabm.9b00034"><strong>Clique aqui</strong></a>
        </li>
    </ul>
    <ul type="disc">
        <li>
            FERREIRA, GUILHERME A. ; Loh, Watson . Planet-Satellite Nanostructures Based on Block Copolymer-Surfactant Nanoparticles Surface-Decorated with Gold and Silver: A New Strategy for Interfacial Catalysis.<strong> Advanced Materials Interfaces,</strong> v. x, p. 1900348, 2019.
            <a href="http://dx.doi.org/10.1002/admi.201900348"><strong>Clique aqui</strong></a>
        </li>
    </ul>
    <ul type="disc">
        <li>
            BALESTRIN, LIA BERALDO DA SILVEIRA ; FRANCISCO, RENATA DIAS ; BERTRAN, CELSO APARECIDO ; CARDOSO, MATEUS BORBA ; Loh, Watson . Direct Assessment of Inhibitor and Solvent Effects on the Deposition Mechanism of Asphaltenes in a Brazilian Crude Oil. <strong>ENERGY &amp; FUELS,</strong> v. x, p. y, 2019.
            <a href="http://dx.doi.org/10.1021/acs.energyfuels.9b00043"><strong>Clique aqui</strong></a>
        </li>
    </ul>
    <ul type="disc">
        <li>
            HEYING, RENATA S. ; DA SILVA, MARCOS PAULO ; WECKER, GIOVANA S. ; PERALTA, Rosely A. ; BORTOLUZZI, Adailton J. ; Neves, Ademir . Unusual hydrolase-like activity of a mononuclear Fe(III) complex.<strong> INORGANIC CHEMISTRY COMMUNICATIONS,</strong> v. 102, p. 245-250, 2019.
            <a href="http://dx.doi.org/10.1016/j.inoche.2019.01.035"><strong>Clique aqui</strong></a>
        </li>
    </ul>

    <ul type="disc">
        <li>
            WESTPHAL, Eduard ; Gallardo, Hugo ; SEBASTIÁN, NEREA ; EREMIN, ALEXEY ; PREHM, MARKO ; ALAASAR, MOHAMED ; TSCHIERSKE, CARSTEN . Liquid crystalline self-assembly of 2,5-diphenyl-1,3,4-oxadiazole based bent-core molecules and the influence of carbosilane end-groups.<strong> Journal of Materials Chemistry C,</strong> v. 7, p. 3064-3081, 2019.
            <a href="http://dx.doi.org/10.1039/C8TC06591H"><strong>Clique aqui</strong></a>
        </li>
    </ul>
"""

soup = BeautifulSoup(html, "html.parser")
text_list = soup.find_all('li')
link_list = soup.find_all('a')

json_file = []

for text, link in list(zip(text_list, link_list)):
    artigo = {}
    text = text.text
    link = link.get('href')
    #print("TEXTO: %s\nLINK: %s\n" % (text, link))

    pesq, info = text.split(" . ")   
    #print("pesq: %s\ninfo: %s\n" % (pesq, info)) 

    pesq_list = pesq.split(" ; ")
    cont = 0
    for i in pesq_list:
        i = i.strip()
        pesq_list[cont] = i
        cont = cont + 1
        #print("pesq: %s\n" % (i))
    artigo["autores"] = pesq_list

    title = info.split(".")[0]
    info = info.replace(title, '')
    info = info[1:].strip()
    #print(info)
    artigo["nome"] = title

    info = info.split(".\n")[0]  #ignora "Cique aqui"
    #print(info)
    info = info.split(", ")
    artigo["publicador"] = info[0]
    artigo["versao"] = info[1]
    artigo["paginas"] = info[2]
    artigo["ano"] = int(info[3])

    for key in artigo:
        print(key, "=", artigo[key])

    #inp = input("Ok?")
    #if(inp != ''):
    #    break

    json_file.append(artigo)

with open('jsonForScript.json', 'w') as file:
    json.dump(json_file, file)