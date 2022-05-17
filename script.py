from bs4 import BeautifulSoup
import json

html = """
    <ul type="disc">
        <li>
            SALLA, CRISTIAN A.M. ; BRAGA, HUGO C. ; HEYING, RENATA DA S. ; MARTINS, JEFFERSON S. ; Quirino, Welber G. ; Legnani, Cristiano ; de Souza, Bernardo ; BORTOLUZZI, Adailton J. ; Gallardo, Hugo ; Eccher, Juliana ; Bechtold, Ivan H. . Photocurrent response enhanced by spin-orbit coupling on ruthenium(II) complexes with heavy atom ligands. <strong>Dyes and Pigments,</strong> v. 140, p. 346-353, 2017.
            <a href="http://dx.doi.org/10.1016/j.dyepig.2017.01.059"><strong>Clique aqui</strong></a>

        </li>
    </ul>
    <ul type="disc">
        <li>
            Ferreira, Marli ; NAULET, GUILLAUME ; Gallardo, Hugo ; DECHAMBENOIT, PIERRE ; BOCK, HARALD ; DUROLA, FABIEN . A Naphtho-Fused Double [7]Helicene from a Maleate-Bridged Chrysene Trimer.<strong> Angewandte Chemie (International ed. Print),</strong> v. 56, p. 3379-3382, 2017.
            <a href="http://dx.doi.org/10.1002/anie.201610793"><strong>Clique aqui</strong></a>
            
        </li>
    </ul>
    <ul type="disc">
        <li>
            BELARMINO'CABRAL, MAR�LIA GABRIELA ; PEREIRA'DE'OLIVEIRA'SANTOS, DEISE MARIA ; CRISTIANO, Rodrigo ; Gallardo, Hugo ; BENTALEB, AHMED ; HILLARD, ELIZABETH A. ; DUROLA, FABIEN ; BOCK, HARALD . From 1,4-Phenylenebis(phenylmaleate) to a Room-Temperature Liquid-Crystalline Benzo[ ]perylene Diimide. <strong>ChemPlusChem</strong>, v. 82, p. 342-346, 2017.
            <a href="http://dx.doi.org/10.1002/cplu.201600566"><strong>Clique aqui</strong></a>

        </li>
    </ul>
    <ul type="disc">
        <li>
            SMANIOTTO, ALESSANDRA ; MEZALIRA, DANIELA Z. ; ZAPP, EDUARDO ; Gallardo, Hugo ; VIEIRA, IOLANDA C. . Electrochemical immunosensor based on an azo compound for thyroid-stimulating hormone detection.<strong> MICROCHEMICAL JOURNAL</strong>, v. 133, p. 510-517, 2017.
            <a href="http://dx.doi.org/10.1016/j.microc.2017.04.010"><strong>Clique aqui</strong></a>
            
        </li>
    </ul>
    <ul type="disc">
        <li>
            MOREIRA, THAMIRES S. ; Ferreira, Marli ; DALL'ARMELLINA, ALICE ; CRISTIANO, Rodrigo ; Gallardo, Hugo ; HILLARD, ELIZABETH A. ; BOCK, HARALD REINHART ; DUROLA, FABIEN . Tetracarboxy-functionalized [8], [10], [12] and [14]Phenacenes. <strong>EUROPEAN JOURNAL OF ORGANIC CHEMISTRY</strong>, v. 31, p. 4548-4551, 2017.
            <a href="http://dx.doi.org/10.1002/ejoc.201700893"><strong>Clique aqui</strong></a>
            
        </li>
    </ul>
    <ul type="disc">
        <li>
            Girotto, Edivandro ; BEHRAMAND, B. ; Bechtold, Ivan H. ; Gallardo, Hugo . Thiophene-based bent-shaped luminescent liquid crystals: synthesis and characterisation. <strong>LIQUID CRYSTALS,</strong> v. 44, p. 1231-1239, 2017.
            <a href="http://dx.doi.org/10.1080/02678292.2016.1272723"><strong>Clique aqui</strong></a>
            
        </li>
    </ul>
    <ul type="disc">
        <li>
            COELHO, RAFAEL L. ; WESTPHAL, Eduard ; MEZALIRA, DANIELA Z. ; Gallardo, Hugo . Polycatenar liquid crystals based on bent-shaped chalcone and cyanopyridine molecules.<strong> LIQUID CRYSTALS</strong>, v. 44, p. 405-416, 2017.
            <a href="http://dx.doi.org/10.1080/02678292.2016.1216185"><strong>Clique aqui</strong></a>

        </li>
    </ul>
    <ul type="disc">
        <li>
            Ferreira, M. ; WESTPHAL, Eduard ; Ballottin, M. V. ; Bechtold, Ivan H ; BARTOLUZZI, A. J. ; MEZALIRA, DANIELA Z. ; Gallardo, H. . Columnar bent-core liquid crystals with two oxadiazole units and two or four alkyl chains and their phase-dependent fluorescence. <strong>NEW JOURNAL OF CHEMISTRY</strong>, v. 41, p. 11766-11777, 2017.
            <a href="http://dx.doi.org/10.1039/c7nj00548b"><strong>Clique aqui</strong></a>

        </li>
    </ul>
    <ul type="disc">
        <li>
            RATTO NETO, C. A. ; Westphal, E ; Gallardo, H. . ( -phenyltriazole) derivative - New compound with star shaped anisometry and discotic liquid crystals behavior. MOLECULAR <strong>CRYSTALS AND LIQUID CRYSTALS,</strong> v. 657, p. 147-155, 2017.
            <a href="http://dx.doi.org/10.1080/15421406.2017.1403807"><strong>Clique aqui</strong></a>
        </li>
    </ul>
    <ul type="disc">
        <li>
            GONÇALVES, BRUNA LISBOA ; GERVINI, VANESSA CARRATU ; FLORES, ALEX FABIANI CLARO ; JUNIOR, JORGE LUIZ PIMENTEL ; BORTOLUZZI, ADAILTON JO�O ; BURROW, ROBERT ALAN ; DUARTE, RAFAEL ; DA SILVA, ROBSON RICARDO ; VICENTI, JULIANO ROSA DE MENEZES . Formation of a new copper(II) dimer through heterocyclic ligand ring opening reaction: Supramolecular features and magnetic properties. <strong>Journal of Molecular Structure (Print)</strong>, v. 1128, p. 410-418, 2017.
            <a href="http://dx.doi.org/10.1016/j.molstruc.2016.09.014"><strong>Clique aqui</strong></a>

        </li>
    </ul>
    <ul type="disc">
        <li>
            SCHRAMM, ADRIANA D.S. ; NICOLETI, CELSO R. ; STOCK, RAFAELA I. ; HEYING, RENATA S. ; Bortoluzzi, Adailton J. ; Machado, Vanderlei G. . Anionic optical devices based on 4-(nitrostyryl)phenols for the selective detection of fluoride in acetonitrile and cyanide in water. Sensors and Actuators<strong> B: Chemical</strong>, v. 240, p. 1036-1048, 2017.
            <a href="http://dx.doi.org/10.1016/j.snb.2016.09.052"><strong>Clique aqui</strong></a>
            
        </li>
    </ul>
    <ul type="disc">
        <li>
            SALLA, CRISTIAN A.M. ; BRAGA, HUGO C. ; HEYING, RENATA DA S. ; MARTINS, JEFFERSON S. ; QUIRINO, WELBER G. ; Legnani, Cristiano ; de Souza, Bernardo ; Bortoluzzi, Adailton J. ; GALLARDO, Hugo ; ECCHER, JULIANA ; Bechtold, Ivan H. . Photocurrent response enhanced by spin-orbit coupling on ruthenium(II) complexes with heavy atom ligands. <strong>DYES AND PIGMENTS,</strong> v. 140, p. 346-353, 2017.
            <a href="http://dx.doi.org/10.1016/j.dyepig.2017.01.05"><strong>Clique aqui</strong></a>
            
        </li>
    </ul>
    <ul type="disc">
        <li>
            AHMAD, M. ; PERVEEN, Z. ; BORTOLUZZI, A. J. ; HAMEED, S. ; SHAH, M. R. ; TARIQ, M. ; UD DIN, G. ; ANWAR, M. . Structural diversities and preliminary antimicrobial studies of 1-((E)-(pentylimino)methyl)naphthalen-2-ol and its metal complexes. <strong>JOURNAL OF STRUCTURAL CHEMISTRY</strong>, v. 58, p. 297-303, 2017.
            <a href="http://dx.doi.org/10.1134/S0022476617020111"><strong>Clique aqui</strong></a>
            
        </li>
    </ul>
    <ul type="disc">
        <li>
            Bortoluzzi, Adailton J.; SILVEIRA, GUSTAVO P. ; S�, Marcus M. . Crystal structure of 5- O -benzoyl-2,3- O -isopropylidene- D -ribono-1,4-lactone.<strong> ACTA CRYSTALLOGRAPHICA SECTION E: CRYSTALLOGRAPHIC COMMUNICATIONS, </strong>v. 73, p. 407-409, 2017.
            <a href="http://dx.doi.org/10.1107/s2056989017002043"><strong>Clique aqui</strong></a>
            
        </li>
    </ul>
    <ul type="disc">
        <li>
            VELASQUES, JECIKA MACIEL ; GERVINI, VANESSA CARRATU ; BORTOLUZZI, ADAÍLTON JOÃO ; FARIAS, RENAN LIRA DE ; OLIVEIRA, ADRIANO BOF DE . Crystal structure of (3 E )-5-nitro-3-(2-phenylhydrazinylidene)-1 H -indol-2(3 H )-one.<strong> ACTA CRYSTALLOGRAPHICA SECTION E: CRYSTALLOGRAPHIC COMMUNICATIONS,</strong> v. 73, p. 168-172, 2017.
            <a href="http://dx.doi.org/10.1107/s2056989016020375"><strong>Clique aqui</strong></a>
            
        </li>
    </ul>
    <ul type="disc">
        <li>
            COSTIN, TA�SSA A. ; DUTRA, LUIZ G. ; Bortoluzzi, Adailton J. ; S�, Marcus M. . Amine-mediated synthesis of amides from 1,3-dicarbonyl compounds through a domino diazo transfer/aminolysis process. <strong>TETRAHEDRON</strong>, v. 73, p. 4549-4559, 2017.
            <a href="http://dx.doi.org/10.1016/j.tet.2017.06.013"><strong>Clique aqui</strong></a>
            
        </li>
    </ul>
    <ul type="disc">
        <li>
            SILVA, LAIS T. ; AZEREDO, JULIANO B. ; SABA, SUMBAL ; RAFIQUE, JAMAL ; Bortoluzzi, Adailton J. ; BRAGA, ANTONIO L. . Solvent- and Metal-Free Chalcogenation of Bicyclic Arenes Using I 2 /DMSO as Non-Metallic Catalytic System. <strong>EUROPEAN JOURNAL OF ORGANIC CHEMISTRY,</strong> v. 2017, p. 4740-4748, 2017.
            <a href="http://dx.doi.org/10.1002/ejoc.201700744"><strong>Clique aqui</strong></a>
            
        </li>
    </ul>
    <ul type="disc">
        <li>
            FERREIRA, M. ; Westphal, E. ; BALLOTTIN, M. V. ; Bechtold, I. H. ; BORTOLUZZI, A. J. ; MEZALIRA, D. Z. ; GALLARDO, H. . Columnar bent-core liquid crystals with two oxadiazole units and two or four alkyl chains and their phase-dependent fluorescence. <strong>NEW JOURNAL OF CHEMISTRY,</strong> v. 41, p. 11766-11777, 2017.
            <a href="http://dx.doi.org/10.1002/ejoc.201700744"><strong>Clique aqui</strong></a>
            
        </li>
    </ul>
    <ul type="disc">
        <li>
            POLLO, LUIZ A.E. ; FREDERICO, MARISA J. ; Bortoluzzi, Adailton J. ; SILVA, F�TIMA R.M.B. ; Biavatti, Maique W. . A new polyacetylene glucoside from Vernonia scorpioides and its potential antihyperglycemic effect. <strong>CHEMICO-BIOLOGICAL INTERACTIONS,</strong> v. 279, p. 95-101, 2017.
            <a href="http://dx.doi.org/10.1016/j.cbi.2017.11.003"><strong>Clique aqui</strong></a>
            
        </li>
    </ul>

    <ul type="disc">
        <li>
            BECHER, TIAGO B. ; Ornelas, Catia . Nonswellable Injectable Hydrogels Self-Assembled Through Non-Covalent Interactions. <strong>ChemistrySelect</strong>, v. 2, p. 3009-3013, 2017.
            <a href="http://dx.doi.org/10.1002/slct.201700292"><strong>Clique aqui</strong></a>
        </li>
    </ul>
    <ul type="disc">
        <li>
            Oliveira, C. P. ; Prado, W. A. ; Lavayen, V. ; Buttenbender, S. L. ; Beckenkamp, A. ; Martins, B. S. ; L�dtke, D. S. ; Campo, L. F. ; Rodembusch, F. S. ; Buffon, A. ; Pessoa Jr, A. ; Guterres, S. S. ; Pohlmann, A. R. . Bromelain-Functionalized Multiple-Wall Lipid-Core Nanocapsules: Formulation, Chemical Structure and Antiproliferative Effect Against Human Breast Cancer Cells (MCF-7). <strong>Pharmaceutical Research, </strong>v. 34, p. 438-452, 2017.
            <a href="http://dx.doi.org/10.1007/s11095-016-2074-2"><strong>Clique aqui</strong></a>
            
        </li>
    </ul>
    <ul type="disc">
        <li>
            PINTO BROD, LUCIMAR M. ; FRONZA, MARIANA G. ; VARGAS, JAQUELINE PINTO ; L�DTKE, DIOGO S. ; BR�NING, C�SAR AUGUSTO ; SAVEGNAGO, LUCIELLI . Modulation of PKA, PKC, CAMKII, ERK 1/2 pathways is involved in the acute antidepressant-like effect of (octylseleno)-xylofuranoside (OSX) in mice.<strong> Psychopharmacologia (Heidelberg),</strong> v. 234, p. 717-725, 2017.
            <a href="http://dx.doi.org/10.1007/s00213-016-4505-5"><strong>Clique aqui</strong></a>
            
        </li>
    </ul>
    <ul type="disc">
        <li>
            Horn, P. A. ; Braun, R. K. ; Isoppo, V. G. ; Costa, J. S. ; L�dtke, D. S. ; Moro, A. V. . Combining Cu-Catalyzed Hydroboration with Pd-Catalyzed Suzuki Coupling for the One-pot Synthesis of Arylallylamines under Micellar Conditions. <strong>ADVANCED SYNTHESIS &amp; CATALYSIS,</strong> v. 359, p. 2322-2328, 2017.
            <a href="http://dx.doi.org/10.1002/adsc.201700094"><strong>Clique aqui</strong></a>
            
        </li>
    </ul>
    <ul type="disc">
        <li>
            MARTINS, BRUNA S. ; MORO, ANG�LICA V. ; L�DTKE, DIOGO S. . Stereoselective Arylation of Amino Aldehydes: Overriding Natural Substrate Control through Chelation.<strong> JOURNAL OF ORGANIC CHEMISTRY</strong>, v. 82, p. 3334-3340, 2017.
            <a href="http://dx.doi.org/10.1021/acs.joc.7b00215"><strong>Clique aqui</strong></a>
            
        </li>
    </ul>
    <ul type="disc">
        <li>
            Martins, B. S. ; L�dtke, D. S. ; Moro, A. V. . Modelos estereoqu�micos de adi��o � carbonila. QUIMICA NOVA, v. 40, p. 342-352, 2017.
            <a href="google.com">Clique aqui</a>
        </li>
    </ul>
    <ul type="disc">
        <li>
            BALDASSARI, LUCAS LOSS ; DE LA TORRE, AURELIEN ; LI, JING ; L�DTKE, DIOGO SEIBERT ; MAULIDE, NUNO . Ynamide Preactivation Allows a Regio- and Stereoselective Synthesis of &#945;,&#946;-disubstituted Enamides. <strong>ANGEWANDTE CHEMIE-INTERNATIONAL EDITION,</strong> v. 56, p. 15723-15727, 2017.
            <a href="http://dx.doi.org/10.1002/anie.201709128"><strong>Clique aqui</strong></a>
        </li>
    </ul>
    <ul type="disc">
        <li>
            JORA, MANAZAEL Z. ; Cardoso, Marcus V.C. ; Sabadini, Edvaldo . Correlation between viscosity, diffusion coefficient and spin-spin relaxation rate in 1 H NMR of water-alcohols solutions. <strong>JOURNAL OF MOLECULAR LIQUIDS, </strong>v. 238, p. 341-346, 2017.
            <a href="http://dx.doi.org/10.1016/j.molliq.2017.05.006"><strong>Clique aqui</strong></a>

        </li>
    </ul>																		<ul type="disc">
        <li>
            ALVARENGA, BRUNO G. ; RAYNAL, MATTHIEU ; Bouteiller, Laurent ; Sabadini, Edvaldo . Unexpected Solvent Influence on the Rheology of Supramolecular Polymers.<strong> MACROMOLECULES,</strong> v. 50, p. 6631-6636, 2017.
            <a href="http://dx.doi.org/10.1021/acs.macromol.7b00786"><strong>Clique aqui</strong></a>
        </li>
    </ul>
    <ul type="disc">
        <li>
            OLIVEIRA, ALINE A.S. ; COSTA, DEM�TRIO S. ; TEIXEIRA, IVO F. ; PARREIRA, LUCIANA A. ; MENINI, LUCIANO ; Gusevskaya, Elena V. ; MOURA, FL�VIA C.C. . Red mud based gold catalysts in the oxidation of benzyl alcohol with molecular oxygen. <strong>CATALYSIS TODAY</strong>, v. 289, p. 89-95, 2017.
            <a href="http://dx.doi.org/10.1016/j.cattod.2016.10.028"><strong>Clique aqui</strong></a>
            
        </li>
    </ul>
    <ul type="disc">
        <li>
            COTTA, RAFAELA F. ; DA SILVA ROCHA, KELLY A. ; KOZHEVNIKOVA, ELENA F. ; KOZHEVNIKOV, IVAN V. ; Gusevskaya, Elena V. . Coupling of monoterpenic alkenes and alcohols with benzaldehyde catalyzed by silica-supported tungstophosphoric heteropoly acid. <strong>CATALYSIS TODAY</strong>, v. 289, p. 14-19, 2017.
            <a href="http://dx.doi.org/10.1016/j.cattod.2016.07.021"><strong>Clique aqui</strong></a>
            
        </li>
    </ul>
    <ul type="disc">
        <li>
            COTTA, RAFAELA F. ; DA SILVA ROCHA, KELLY A. ; KOZHEVNIKOVA, ELENA F. ; KOZHEVNIKOV, IVAN V. ; Gusevskaya, Elena V. . Heteropoly acid catalysts in upgrading of biorenewables: Cycloaddition of aldehydes to monoterpenes in green solvents.<strong> APPLIED CATALYSIS B-ENVIRONMENTAL,</strong> v. 217, p. 92-99, 2017.
            <a href="http://dx.doi.org/10.1016/j.apcatb.2017.05.055"><strong>Clique aqui</strong></a>
            
        </li>
    </ul>
    <ul type="disc">
        <li>
            PIMENTA, LAURA S. ; Gusevskaya, Elena ; ALBERTO, EDUARDO . Intermolecular Halogenation/Esterification of Alkenes with N-Halosuccinimide and Acetic Acid Catalyzed by DABCO.<strong> ADVANCED SYNTHESIS &amp; CATALYSIS</strong>, v. 359, p. 2297-2303, 2017.
            <a href="http://dx.doi.org/10.1002/adsc.201700117"><strong>Clique aqui</strong></a>
            
        </li>
    </ul>
    <ul type="disc">
        <li>
            PARREIRA, LUCIANA A. ; AZEVEDO, ANA F. ; MENINI, LUCIANO ; Gusevskaya, Elena V. . Functionalization of the naturally occurring linalool and nerol by the palladium catalyzed oxidation of their trisubstituted olefinic bonds. <strong>JOURNAL OF MOLECULAR CATALYSIS A-CHEMICAL</strong>, v. 426, p. 429-434, 2017.
            <a href="http://dx.doi.org/10.1016/j.molcata.2016.07.033"><strong>Clique aqui</strong></a>
            
        </li>
    </ul>
    <ul type="disc">
        <li>
            GARCIA, MARCO A.S. ; IBRAHIM, MAHMOUD ; COSTA, JEAN C.S. ; CORIO, PAOLA ; Gusevskaya, Elena V. ; DOS SANTOS, EDUARDO N. ; PHILIPPOT, KARINE ; ROSSI, LIANE M. . Study of the influence of PPh 3 used as capping ligand or as reaction modifier for hydroformylation reaction involving Rh NPs as precatalyst.<strong> APPLIED CATALYSIS A-GENERAL,</strong> v. 548, p. 136-142, 2017.
            <a href="http://dx.doi.org/10.1016/j.apcata.2017.08.009"><strong>Clique aqui</strong></a>
            
        </li>
    </ul>
    <ul type="disc">
        <li>
            DE CAMARGO FARIA, AMANDA ; DOS SANTOS WANDERLEY, TACIANO A. ; ALBERTO, EDUARDO E. ; Gusevskaya, Elena V. . Palladium catalyzed aerobic oxidation for the incorporation of an olfactory group on naturally occurring &#946;-caryophyllene. <strong>APPLIED CATALYSIS A-GENERAL</strong>, v. 548, p. 33-38, 2017.
            <a href="http://dx.doi.org/10.1016/j.apcata.2017.07.042"><strong>Clique aqui</strong></a>
            
        </li>
    </ul>
    <ul type="disc">
        <li>
            Gusevskaya, Elena V.; DOS SANTOS COSTA, MA�RA ; DE MEIRELES, AUGUSTO L. P. . Aerobic palladium catalyzed oxidations in upgrading of bio-renewables: oxidation of &amp;bta;-ionone and &#945;-ionone. <strong>Asian Journal of Organic Chemistry,</strong> v. 6, p. 1628-1634, 2017.
            <a href="http://dx.doi.org/10.1002/ajoc.201700337"><strong>Clique aqui</strong></a>
            
        </li>
    </ul>
    <ul type="disc">
        <li>
            DE MEIRELES, AUGUSTO L.P. ; DA SILVA ROCHA, KELLY A. ; KOZHEVNIKOVA, ELENA F. ; KOZHEVNIKOV, IVAN V. ; Gusevskaya, Elena V. . Heteropoly acid catalysts for the valorization of biorenewables: Isomerization of caryophyllene oxide in green solvents. <strong>Molecular Catalysis</strong>, v. 458, p. 213-222, 2017.
            <a href="http://dx.doi.org/10.1016/j.mcat.2017.12.019"><strong>Clique aqui</strong></a>
        </li>
    </ul>
    <ul type="disc">
        <li>
            PAIX�O, DRIELLY A. ; MARZANO, IVANA M. ; JAIMES, EDGAR H.L. ; PIVATTO, MARCOS ; CAMPOS, DE�BORA L. ; PAVAN, FERNANDO R. ; DEFLON, VICTOR M. ; MAIA, PEDRO IVO DA S. ; DA COSTA FERREIRA, ANA M. ; UEHARA, ISADORA A. ; SILVA, MARCELO J.B. ; Botelho, Françoise V. ; Pereira-Maia, Elene C. ; GUILARDI, SILVANA ; Guerra, Wendell . Novel copper(II) complexes with hydrazides and heterocyclic bases: Synthesis, structure and biological studies.<strong> JOURNAL OF INORGANIC BIOCHEMISTRY,</strong> v. 172, p. 138-146, 2017.
            <a href="http://dx.doi.org/10.1016/j.jinorgbio.2017.04.024"><strong>Clique aqui</strong></a>
            
        </li>
    </ul>
    <ul type="disc">
        <li>
            GONZ�LEZ-BAR�, ANA C. ; FERRARESI-CUROTTO, VER�NICA ; PIS-DIEZ, REINALDO ; COSTA, BEATRIZ S. PARAJ�N ; RESENDE, JACKSON A.L.C. ; DE PAULA, FL�VIA C.S. ; Pereira-Maia, Elene C. ; Rey, Nicol�s A. . A novel oxidovanadium(V) compound with an isonicotinohydrazide ligand. A combined experimental and theoretical study and cytotoxity against K562 cells..<strong> POLYHEDRON,</strong> v. 135, p. 303-310, 2017.
            <a href="http://dx.doi.org/10.1016/j.poly.2017.07.013"><strong>Clique aqui</strong></a>
            
        </li>
    </ul>
    <ul type="disc">
        <li>
            DA CUNHA, TAMYRIS T. ; OLIVEIRA, WILLIAN X.C. ; MARZANO, IVANA M. ; PINHEIRO, CARLOS B. ; Pereira-Maia, Elene Cristina ; PEREIRA, CYNTHIA L.M. . Topological control of supramolecular crystal structures of phenylene bis-monothiooxamate derivatives and in vitro anticancer activity. <strong>JOURNAL OF MOLECULAR STRUCTURE</strong>, v. 1149, p. 803-811, 2017.
            <a href="http://dx.doi.org/10.1016/j.molstruc.2017.08.051"><strong>Clique aqui</strong></a>
            
        </li>
    </ul>
    <ul type="disc">
        <li>
            MELO, A. C. C. ; SANTANA, J. M. S. V. P. ; NUNES, K. J. R. C. ; MARQUES, M. A. ; OLIVEIRA, G. A. P. ; MORAES, A. H. ; Pereira-Maia, Elene Cristina . Interactions of ruthenium(II) compounds with sulfasalazine and N,N'-heterocyclic ligands with proteins.<strong> INORGANICA CHIMICA ACTA</strong>, v. 467, p. 385-390, 2017.
            <a href="http://dx.doi.org/10.1016/j.ica.2017.08.037"><strong>Clique aqui</strong></a>
            
        </li>
    </ul>
    <ul type="disc">
        <li>
            CAMARGO, TIAGO PACHECO ; Neves, Ademir ; PERALTA, ROSELY A. ; CHAVES, CL�UDIA ; MAIA, ELENE C. P. ; LIZARAZO-JAIMES, EDGAR H. ; GOMES, DAWIDSON A. ; Bortolotto, Tiago ; NORBERTO, DOUGLAS R. ; Terenzi, Hern&amp;aaacute;n ; TIERNEY, DAVID L. ; SCHENK, GERHARD . Second-Sphere Effects in Dinuclear Fe III Zn II Hydrolase Biomimetics: Tuning Binding and Reactivity Properties.<strong> INORGANIC CHEMISTRY,</strong> v. 57, p. 187-203, 2017.
            <a href="http://dx.doi.org/10.1021/acs.inorgchem.7b02384"><strong>Clique aqui</strong></a>

        </li>
    </ul>
    <ul type="disc">
        <li>
            BRAGA, L. R. ; Machado, F . Embalagens Ativas: Uma Nova Abordagem para Embalagens Aliment�cias. <strong>Brazilian Journal of Food Research</strong>, v. 8, p. 170-186, 2017.
            <a href="google.com">Clique aqui</a>
        </li>
    </ul>
    <ul type="disc">
        <li>
            MEDEIROS, ANDERSON M. M. S. ; Machado, Fabricio ; RUBIM, JOEL C. ; MCKENNA, TIMOTHY F. L. . Bio-based copolymers obtained through miniemulsion copolymerization of methyl esters of acrylated fatty acids and styrene. Journal of Polymer Science<strong> Part A: Polymer Chemistry</strong>, v. 55, p. 1422-1432, 2017.
            <a href="http://dx.doi.org/10.1002/pola.28511"><strong>Clique aqui</strong></a>

        </li>
    </ul>
    <ul type="disc">
        <li>
            Machado, Fabricio; VALADARES, LEONARDO ; NEVES, JULIETE . Experimental Study on the Synthesis of Iridescent Copolymers through Emulsion Polymerization.<strong> Current Applied Polymer Science,</strong> v. 01, p. 1-1, 2017.
            <a href="http://dx.doi.org/10.2174/2452271601666170221124329"><strong>Clique aqui</strong></a>

        </li>
    </ul>
    <ul type="disc">
        <li>
            VICTOR, PRISCILLA ARA�JO ; GON�ALVES, S�LVIA BEL�M ; Machado, Fabricio . Styrene/Lignin-Based Polymeric Composites Obtained Through a Sequential Mass-Suspension Polymerization Process.<strong> JOURNAL OF POLYMERS AND THE ENVIRONMENT,</strong> v. 25, p. n/a, 2017.
            <a href="http://dx.doi.org/10.1007/s10924-017-1078-2"><strong>Clique aqui</strong></a>

        </li>
    </ul>
    <ul type="disc">
        <li>
            P�RES, EDUARDO ULISSES XAVIER ; SOUSA, MARCELO HENRIQUE ; GOMES DE SOUZA, FERNANDO ; Machado, Fabricio ; SUAREZ, PAULO ANSELMO ZIANI . Synthesis and characterization of a new biobased poly(urethane-ester) from ricinoleic acid and its use as biopolymeric matrix for magnetic nanocomposites. <strong>EUROPEAN JOURNAL OF LIPID SCIENCE AND TECHNOLOGY, </strong>v. 119, p. 1600451, 2017.
            <a href="http://dx.doi.org/10.1002/ejlt.201600451"><strong>Clique aqui</strong></a>

        </li>
    </ul>
    <ul type="disc">
        <li>
            COSTA, RAPHAEL MARIA DIAS DA ; HUNGERB�HLER, GABRIELA ; SARAIVA, THIAGO ; DE JONG, GABRIEL ; MORAES, RAFAEL SILVA ; FURTADO, EVANDRO GON�ALVES ; SILVA, FABR�CIO MACHADO ; OLIVEIRA, GEIZA ESPERANDIO DE ; FERREIRA, LUCIANA SPINELLI ; SOUZA JUNIOR, FERNANDO GOMES DE . Green polyurethane synthesis by emulsion technique: a magnetic composite for oil spill removal. <strong>Polimeros-Ciencia e Tecnologia</strong>, v. 27, p. 273-279, 2017.
            <a href="http://dx.doi.org/10.1590/0104-1428.2397"><strong>Clique aqui</strong></a>

        </li>
    </ul>
    <ul type="disc">
        <li>
            BRAGA, LILIAN RODRIGUES ; RANGEL, ELLEN TANUS ; SUAREZ, PAULO ANSELMO ZIANI ; Machado, Fabricio . Simple synthesis of active films based on PVC incorporated with silver nanoparticles: Evaluation of the thermal, structural and antimicrobial properties.<strong> FOOD PACKAGING AND SHELF LIFE</strong>, v. n/a, p. n/a, 2017.
            <a href="http://dx.doi.org/10.1016/j.fpsl.2017.12.005"><strong>Clique aqui</strong></a>

        </li>
    </ul>
    <ul type="disc">
        <li>
            NETO, WESLANY SILV�RIO ; DUTRA, GABRIEL VICTOR SIM�ES ; JENSEN, ALAN THYAGO ; ARA�JO, OLACIR ALVES ; GARG, VIJAYENDRA ; DE OLIVEIRA, ADERBAL CARLOS ; VALADARES, LEONARDO FONSECA ; DE SOUZA, FERNANDO GOMES ; Machado, Fabricio . Superparamagnetic nanoparticles stabilized with free-radical polymerizable oleic acid-based coating. <strong>JOURNAL OF ALLOYS AND COMPOUNDS,</strong> v. n/a, p. n/a, 2017.
            <a href="http://dx.doi.org/10.1016/j.jallcom.2017.12.338"><strong>Clique aqui</strong></a>
        </li>
    </ul>
    <ul type="disc">
        <li>
            SANTOS BUBNIAK, LORENA DOS ; GASPAR, P�MELA CRISTINA ; DE MORAES, ANA CAROLINA RABELLO ; BIGOLIN, ALISSON ; DE SOUZA, RUBIA KARINE ; BUZZI, F�TIMA CAMPOS ; CORR&amp;Ecerc;A, ROG�RIO ; FILHO, VALDIR CECHINEL ; BRETANHA, LIZANDRA CZERMAINSKI ; Micke, Gustavo Amadeu ; NUNES, RICARDO JOS� ; SANTOS-SILVA, MARIA CL�UDIA . Effects of 1,3,5-triphenyl-4,5-dihydro-1 H -pyrazole derivatives on cell-cycle and apoptosis in human acute leukemia cell lines. <strong>CANADIAN JOURNAL OF PHYSIOLOGY AND PHARMACOLOGY,</strong> v. 95, p. 548-563, 2017.
            <a href="http://dx.doi.org/10.1139/cjpp-2016-0222"><strong>Clique aqui</strong></a>
            
        </li>
    </ul>
    <ul type="disc">
        <li>
            DUARTE, LUCAS M. ; PASCHOAL, DIEGO ; IZUMI, CELLY M.S. ; DOLZAN, MARESSA D. ; ALVES, VICTOR R. ; Micke, Gustavo A. ; DOS SANTOS, H�LIO F. ; DE OLIVEIRA, MARCONE A.L. . Simultaneous determination of aspartame, cyclamate, saccharin and acesulfame-K in powder tabletop sweeteners by FT-Raman spectroscopy associated with the multivariate calibration: PLS, iPLS and siPLS models were compared. <strong>FOOD RESEARCH INTERNATIONAL</strong>, v. 01, p. 01-0001, 2017.
            <a href="http://dx.doi.org/10.1016/j.foodres.2017.05.006"><strong>Clique aqui</strong></a>
            
        </li>
    </ul>
    <ul type="disc">
        <li>
            Caon, Thiago ; KRATZ, JADEL MULLER ; KUMINEK, GISLAINE ; Heller, Melina ; Micke, Gustavo Amadeu ; DE ARAUJO, BIBIANA VERLINDO ; KOESTER, LET�CIA SCHERER ; Sim�es, Cl�udia Maria Oliveira . Pharmacokinetics of Saquinavir Mesylate from Oral Self-Emulsifying Lipid-Based Delivery Systems.<strong> EUROPEAN JOURNAL OF DRUG METABOLISM AND PHARMACOKINETICS</strong>, v. 42, p. 135-141, 2017.
            <a href="http://dx.doi.org/10.1007/s13318-016-0321-x"><strong>Clique aqui</strong></a>
            
        </li>
    </ul>
    <ul type="disc">
        <li>
            SCHULZ, MAYARA ; BILUCA, FAB�OLA CARINA ; Gonzaga, Luciano Valdemiro ; BORGES, GRACIELE DA SILVA CAMPELO ; Vitali, Luciano ; Micke, Gustavo Amadeu ; DE GOIS, JEFFERSON SANTOS ; DE ALMEIDA, TARCISIO SILVA ; BORGES, DANIEL LAZARO GALLINDO ; MILLER, PAUL RICHARD MOMSEN ; COSTA, Ana Carolina Oliveira ; Fett, Roseane . Bioaccessibility of bioactive compounds and antioxidant potential of juçara fruits ( Euterpe edulis Martius) subjected to in vitro gastrointestinal digestion. <strong>FOOD CHEMISTRY,</strong> v. 228, p. 447-454, 2017.
            <a href="http://dx.doi.org/10.1016/j.foodchem.2017.02.038"><strong>Clique aqui</strong></a>
            
        </li>
    </ul>
    <ul type="disc">
        <li>
            GRINEVICIUS, VALDEL�CIA M.A.S. ; ANDRADE, K�TIA S. ; OURIQUE, FABIANA ; Micke, Gustavo A. ; FERREIRA, SANDRA R.S. ; PEDROSA, ROZANGELA C. . Antitumor activity of conventional and supercritical extracts from Piper nigrum L. cultivar Bragantina through cell cycle arrest and apoptosis induction. <strong>JOURNAL OF SUPERCRITICAL FLUIDS, </strong>v. 128, p. 94-101, 2017.
            <a href="http://dx.doi.org/10.1016/j.supflu.2017.05.009"><strong>Clique aqui</strong></a>
            
        </li>
    </ul>
    <ul type="disc">
        <li>
            SIEBERT, DIOGO A. ; BASTOS, JULIANA ; SPUDEIT, DANIEL A. ; Micke, Gustavo A. ; ALBERTON, MICHELE D. . Determination of phenolic profile by HPLC-ESI-MS/MS and anti-inflammatory activity of crude hydroalcoholic extract and ethyl acetate fraction from leaves of Eugenia brasiliensis.<strong> Revista Brasileira de Farmacognosia-Brazilian Journal of Pharmacognosy</strong>, v. 01, p. 01-0001, 2017.
            <a href="http://dx.doi.org/10.1016/j.bjp.2017.01.008"><strong>Clique aqui</strong></a>
            
        </li>
    </ul>
    <ul type="disc">
        <li>
            DE DEA LINDNER, JULIANO ; PAGGI, DAIANE ; PINTO, VINICIUS DUARTE ; SOARES, DOUGLAS ; DOLZAN, MARESSA DANIELI ; BEVACQUA, DANIELLE ; Micke, Gustavo Amadeu ; OLIVEIRA, JOSE VLADIMIR . A Novel Functional Fruit/Vegetable Beverage for the Elderly: Development and Evaluation of Different Preservation Processes on Functional and Enriched Components and Microorganisms.<strong> JOURNAL OF FOOD RESEARCH,</strong> v. 6, p. 17, 2017.
            <a href="http://dx.doi.org/10.5539/jfr.v6n4p17"><strong>Clique aqui</strong></a>
            
        </li>
    </ul>
    <ul type="disc">
        <li>
            Vitali, Luciano ; GON�ALVES, SAMANTHA ; RODRIGUES, VICTOR ; F�vere, Valfredo T. ; Micke, Gustavo A. . Development of a fast method for simultaneous determination of hippuric acid, mandelic acid, and creatinine in urine by capillary zone electrophoresis using polymer multilayer-coated capillary. <strong>ANALYTICAL AND BIOANALYTICAL CHEMISTRY,</strong> v. 409, p. 1943-1950, 2017.
            <a href="http://dx.doi.org/10.1007/s00216-016-0142-4"><strong>Clique aqui</strong></a>
            
        </li>
    </ul>
    <ul type="disc">
        <li>
            BILUCA, FAB�OLA CARINA ; DE GOIS, JEFFERSON SANTOS ; SCHULZ, MAYARA ; BRAGHINI, FRANCIELI ; Gonzaga, Luciano Valdemiro ; MALTEZ, HELOISA FRAN�A ; RODRIGUES, ELISEU ; Vitali, Luciano ; Micke, Gustavo Amadeu ; BORGES, DANIEL L.G. ; COSTA, Ana Carolina Oliveira ; Fett, Roseane . Phenolic compounds, antioxidant capacity and bioaccessibility of minerals of stingless bee honey ( Meliponinae ). <strong>JOURNAL OF FOOD COMPOSITION AND ANALYSIS</strong>, v. 63, p. 89-97, 2017.
            <a href="http://dx.doi.org/10.1016/j.jfca.2017.07.039"><strong>Clique aqui</strong></a>
            
        </li>
    </ul>
    <ul type="disc">
        <li>
            CARNEIRO, N�RGELLA S. ; ALVES, CASSIA C.F. ; ALVES, JOS� M. ; EGEA, MARIANA B. ; MARTINS, CARLOS H.G. ; SILVA, THAYN� S. ; BRETANHA, LIZANDRA C. ; BALLESTE, MAIRA P. ; Micke, Gustavo A. ; SILVEIRA, EDUARDO V. ; MIRANDA, MAYKER L.D. . Chemical composition, antioxidant and antibacterial activities of essential oils from leaves and flowers of Eugenia klotzschiana Berg (Myrtaceae). <strong>ANAIS DA ACADEMIA BRASILEIRA DE CIENCIAS</strong>, v. xx, p. 2-9, 2017.
            <a href="http://dx.doi.org/10.1590/0001-3765201720160652"><strong>Clique aqui</strong></a>
            
        </li>
    </ul>
    <ul type="disc">
        <li>
            CHAABAN, AMANDA ; MARTINS, CARLOS EDUARDO NOGUEIRA ; BRETANHA, LIZANDRA CZERMAINSKI ; Micke, Gustavo Amadeu ; CARRER, ALESSANDRA REGINA ; ROSA, NATH�LIA FRANÇA ; FERREIRA, LUISA ; MOLENTO, MARCELO BELTR�O . Insecticide activity of Baccharis dracunculifolia essential oil against Cochliomyia macellaria (Diptera: Calliphoridae).<strong> NATURAL PRODUCT RESEARCH,</strong> v. 1, p. 1-5, 2017.
            <a href="http://dx.doi.org/10.1080/14786419.2017.1392947"><strong>Clique aqui</strong></a>
            
        </li>
    </ul>
    <ul type="disc">
        <li>
            TENFEN, A. ; SIEBERT, DIOGO A. ; SPUDEIT, DANIEL A. ; CORDOVA, C. M. M. ; MICKE, G. A. ; ALBERTON, MICHELE D. . Determination of phenolic profile by HPLC-ESI-MS/MS and antibacterial activity of Eugenia platysema against mollicutes strains.<strong> JOURNAL OF APPLIED PHARMACEUTICAL SCIENCE</strong>, v. -, p. 007-011, 2017.
            <a href="http://dx.doi.org/10.7324/JAPS.2017.70502"><strong>Clique aqui</strong></a>
            
        </li>
    </ul>
    <ul type="disc">
        <li>
            BETTANIN, LUANA ; SABA, SUMBAL ; GALETTO, F�BIO Z. ; MIKE, GUSTAVO A. ; RAFIQUE, JAMAL ; BRAGA, ANTONIO L. . Solvent- and metal-free selective oxidation of thiols to disulfides using I 2 /DMSO catalytic system. <strong>TETRAHEDRON LETTERS,</strong> v. 58, p. 4713-4716, 2017.
            <a href="http://dx.doi.org/10.1016/j.tetlet.2017.11.009"><strong>Clique aqui</strong></a>
            
        </li>
    </ul>
    <ul type="disc">
        <li>
            PAULETI, NATHIELLI NAYARA ; MELLO, JONAS ; SIEBERT, DIOGO ALEXANDRE ; Micke, Gustavo Amadeu ; DE ALBUQUERQUE, CL�UDIA ALMEIDA COELHO ; ALBERTON, MICHELE DEBIASI ; BARAUNA, SARA CRISTIANE . Characterisation of phenolic compounds of the ethyl acetate fraction from Tabernaemontana catharinensis and its potential antidepressant-like effect.<strong> NATURAL PRODUCT RESEARCH,</strong> v. 32, p. 1-4, 2017.
            <a href="http://dx.doi.org/10.1080/14786419.2017.1359167"><strong>Clique aqui</strong></a>

        </li>
    </ul>
    <ul type="disc">
        <li>
            BAGGIO, ALAN R. ; Machado, Daniel F. S. ; CARVALHO-SILVA, VALTER H. ; PATERNO, LEONARDO G. ; DE OLIVEIRA, HEIBBE CRISTHIAN B. . Rovibrational spectroscopic constants of the interaction between ammonia and metallo-phthalocyanines: a theoretical protocol for ammonia sensor design. <strong>PHYSICAL CHEMISTRY CHEMICAL PHYSICS</strong>, v. 1, p. 1-1, 2017.
            <a href="http://dx.doi.org/10.1039/c6cp07900h"><strong>Clique aqui</strong></a>
            
        </li>
    </ul>
    <ul type="disc">
        <li>
            ALMEIDA, LEONARDO R. ; ANJOS, MURILO M. ; RIBEIRO, GABRIELA C. ; VALVERDE, CLODOALDO ; Machado, Daniel F. S. ; Oliveira, Guilherme R. ; NAPOLITANO, HAMILTON B. ; DE OLIVEIRA, HEIBBE C. B. . Synthesis, structural characterization and computational study of a novel amino chalcone: a potential nonlinear optical material. <strong>NEW JOURNAL OF CHEMISTRY,</strong> v. 41, p. 1744-1754, 2017.
            <a href="http://dx.doi.org/10.1039/c5nj03214h"><strong>Clique aqui</strong></a>
            
        </li>
    </ul>
    <ul type="disc">
        <li>
            RODRIGUES, THYAGO S. ; LESAGE, DENIS ; DA SILVA, WENDER A. ; COLE, RICHARD B. ; EBELING, G�NTER ; DUPONT, JA�RTON ; DE OLIVEIRA, HEIBBE C. B. ; EBERLIN, MARCOS N. ; Neto, Brenno A. D. . Charge-tagged N-heterocyclic carbenes (NHC): Direct transfer from ionic liquid solutions and long-lived nature in the gas phase.<strong>JOURNAL OF THE AMERICAN SOCIETY FOR MASS SPECTROMETRY,</strong> v. 28, p. 1021-1029, 2017.
            <a href="http://dx.doi.org/10.1007/s13361-017-1637-8"><strong>Clique aqui</strong></a>
            
        </li>
    </ul>
    <ul type="disc">
        <li>
            VALVERDE, CLODOALDO ; RODRIGUES, ROSEMBERG F. N. ; Machado, Daniel F. S. ; BASEIA, BAS�LIO ; DE OLIVEIRA, HEIBBE C. B. . Effect of the crystalline environment on the third-order nonlinear optical properties of L-arginine phosphate monohydrate: a theoretical study. <strong>JOURNAL OF MOLECULAR MODELING,</strong> v. 23, p. 122, 2017.
            <a href="http://dx.doi.org/10.1007/s00894-017-3274-3"><strong>Clique aqui</strong></a>
            
        </li>
    </ul>
    <ul type="disc">
        <li>
            Machado, Daniel F. S. ; SILVA, RODRIGO A. L. ; DE OLIVEIRA, ANA PAULA ; CARVALHO-SILVA, VALTER H. ; Gargano, Ricardo ; Ribeiro, Luciano ; DE OLIVEIRA, HEIBBE C. B. . A novel analytical potential function for dicationic diatomic molecular systems based on deformed exponential function.<strong> JOURNAL OF MOLECULAR MODELING,</strong> v. 23, p. 182, 2017.
            <a href="http://dx.doi.org/10.1007/s00894-017-3339-3"><strong>Clique aqui</strong></a>

        </li>
    </ul>
    <ul type="disc">
        <li>
            Jurberg, Igor Dias . An Aminocatalyzed Stereoselective Strategy for the Formal alpha-Propargylation of Ketones. <strong>CHEMISTRY-A EUROPEAN JOURNAL,</strong> v. 23, p. 9716-9720, 2017.
            <a href="http://dx.doi.org/10.1002/chem.201701433"><strong>Clique aqui</strong></a>

        </li>
    </ul>
    <ul type="disc">
        <li>
            Jurberg, Igor D.; DAVIES, HUW M. L. . Rhodium- and Non-Metal-Catalyzed Approaches for the Conversion of Isoxazol-5-ones to 2,3-Dihydro-6 -1,3-oxazin-6-ones.<strong> ORGANIC LETTERS, </strong>v. 19, p. 5158-5161, 2017.
            <a href="http://dx.doi.org/10.1021/acs.orglett.7b02436"><strong>Clique aqui</strong></a>
            
        </li>
    </ul>
    <ul type="disc">
        <li>
            STIVANIN, MATEUS L. ; DUARTE, MARCELO ; SARTORI, CAMILA ; CAPRETI, NAYLIL M. R. ; ANGOLINI, CELIO F. F. ; Jurberg, Igor D. . An Aminocatalyzed Michael Addition/Iron-mediated Decarboxylative Cyclization Sequence for the Preparation of 2,3,4,6-Tetrasubstituted Pyridines: Scope and Mechanistic Insights.<strong> JOURNAL OF ORGANIC CHEMISTRY,</strong> v. -, p. 10319-10330, 2017.
            <a href="http://dx.doi.org/10.1021/acs.joc.7b01789"><strong>Clique aqui</strong></a>
        </li>
    </ul>
    <ul type="disc">
        <li>
            MANJUNATH, KRISHNAPPA ; SOUZA, VIRG�NIA S. ; GANGANAGAPPA, NAGARAJU ; SCHOLTEN, JACKSON D. ; TEIXEIRA, S�RGIO R. ; Dupont, Jairton ; THIPPESWAMY, RAMAKRISHNAPPA . Effect of the magnetic core of (MnFe) 2 O 3 @Ta 2 O 5 nanoparticles on photocatalytic hydrogen production. <strong>New Journal of Chemistry (1987)</strong>, v. 41, p. 326-334, 2017.
            <a href="http://dx.doi.org/10.1039/c6nj03137d"><strong>Clique aqui</strong></a>

        </li>
    </ul>
    <ul type="disc">
        <li>
            WEILHARD, ANDREAS ; ABARCA, GABRIEL ; VISCARDI, JANINE ; Prechtl, Martin H. G. ; SCHOLTEN, JACKSON D. ; BERNARDI, FABIANO ; BAPTISTA, DANIEL L. ; Dupont, Jairton . Challenging Thermodynamics: Hydrogenation of Benzene to 1,3-Cyclohexadiene by Ru@Pt Nanoparticles. <strong>ChemCatChem,</strong> v. 9, p. 204-211, 2017.
            <a href="http://dx.doi.org/10.1002/cctc.201601196"><strong>Clique aqui</strong></a>
            
        </li>
    </ul>
    <ul type="disc">
        <li>
            CLAUDINO, THIAGO S. ; SCHOLTEN, JACKSON D. ; MONTEIRO, ADRIANO L. . Selective Pd-catalyzed hydrogenation of 3,3-diphenylallyl alcohol: Efficient synthesis of 3,3-diarylpropylamine drugs diisopromine and feniprane.<strong> CATALYSIS COMMUNICATIONS,</strong> v. 102, p. 53-56, 2017.
            <a href="http://dx.doi.org/10.1016/j.catcom.2017.08.025%3Cstrong%3E"><strong>Clique aqui</strong></a>
            
        </li>
    </ul>
    <ul type="disc">
        <li>
            GALDINO, NATH�LIA M. ; BREHM, GABRIELE S. ; BUSSAMARA, ROBERTA ; GON�ALVES, WELLINGTON D. G. ; ABARCA ANJARI, GABRIEL ABARCA ; SCHOLTEN, JACKSON D. . Sputtering deposition of gold nanoparticles onto graphene oxide functionalized with ionic liquids: biosensor materials for cholesterol detection.<strong> Journal of Materials Chemistry B</strong>, v. 5, p. 9482-9486, 2017.
            <a href="http://dx.doi.org/10.1039/c7tb02582c"><strong>Clique aqui</strong></a>
            
        </li>
    </ul>
    <ul type="disc">
        <li>
            CERRUTTI, B.M. ; ZAMBON, M. ; MEGIATTO, J.D. ; FROLLINI, E. . Synthesis of carboxymethylcelluloses with different degrees of substitution and their performance as renewable stabilizing agents for aqueous ceramic suspensions. <strong>INDUSTRIAL CROPS AND PRODUCTS</strong>, v. 107, p. 54-62, 2017.
            <a href="http://dx.doi.org/10.1016/j.indcrop.2017.05.029"><strong>Clique aqui</strong></a>
        </li>
    </ul>
    <ul type="disc">
        <li>											
            D?HENI TEIXEIRA, MARIA BET�NIA ; DUARTE, MARCO ANT�NIO B. ; RAPOSO GARCEZ, LOUREINE ; CAMARGO RUBIM, JOEL ; HOFMANN GATTI, TH�R�SE ; SUAREZ, PAULO ANSELMO ZIANI . Process development for cigarette butts recycling into cellulose pulp.<strong> Waste Management (Elmsford)</strong>, v. 60, p. 140-150, 2017.
            <a href="http://dx.doi.org/10.1016/j.wasman.2016.10.013"><strong>Clique aqui</strong></a>

        </li>
    </ul>
    <ul type="disc">
        <li>
            MEDEIROS, ANDERSON M. M. S. ; MACHADO, FABRICIO ; Rubim, Joel C. ; MCKENNA, TIMOTHY F. L. . Bio-based copolymers obtained through miniemulsion copolymerization of methyl esters of acrylated fatty acids and styrene. Journal of Polymer Science<strong> Part A: Polymer Chemistry,</strong> v. 55, p. 1422-1432, 2017.
            <a href="http://dx.doi.org/10.1002/pola.28511"><strong>Clique aqui</strong></a>
        </li>
    </ul>
    <ul type="disc">
        <li>
            PLIEGO, J. R. . Molecular dynamics and cluster-continuum insights on bulk alcohols effects on S N 2 reactions of potassium and cesium fluorides with alkyl halides. <strong>JOURNAL OF MOLECULAR LIQUIDS</strong>, v. 237, p. 157-163, 2017.
            <a href="http://dx.doi.org/10.1016/j.molliq.2017.04.089"><strong>Clique aqui</strong></a>

        </li>
    </ul>
    <ul type="disc">
        <li>
            DALESSANDRO, ELLEN VASCONCELOS ; COLLIN, HUGO PAUL ; GUIMARÃES, LUIZ GUSTAVO L. ; VALLE, MARCELO SIQUEIRA ; Pliego, Josefredo Rodriguez . Mechanism of the Piperidine-Catalyzed Knoevenagel Condensation Reaction in Methanol: The Role of Iminium and Enolate Ions. <strong>JOURNAL OF PHYSICAL CHEMISTRY B</strong>, v. 121, p. 5300-5307, 2017.
            <a href="http://dx.doi.org/10.1021/acs.jpcb.7b03191"><strong>Clique aqui</strong></a>
            
        </li>
    </ul>
    <ul type="disc">
        <li>
            PLIEGO, J. R. . Cluster expansion of the solvation free energy difference: Systematic improvements in the solvation of single ions.<strong>JOURNAL OF CHEMICAL PHYSICS</strong>, v. 147, p. 034104, 2017.
            <a href="http://dx.doi.org/10.1063/1.4993770"><strong>Clique aqui</strong></a>
            
        </li>
    </ul>

    <ul type="disc">
        <li>
            COSTA, JEAN C. S. ; GON�ALVES, RENATO V. ; TEIXEIRA-NETO, �RICO ; Rossi, Liane M. . Temperature-Driven Restructuring of Silver on AuAg Porous Nanotubes: Impact on CO Oxidation.<strong> ChemistrySelect</strong>, v. 2, p. 660-664, 2017.
            <a href="http://dx.doi.org/10.1002/slct.201601512"><strong>Clique aqui</strong></a>
            
        </li>
    </ul>
    <ul type="disc">
        <li>
            EFFENBERGER, FERNANDO B ; COUTO, RICARDO A ; KIYOHARA, PEDRO K ; Machado, Giovanna ; MASUNAGA, SUELI H ; JARDIM, RENATO F ; Rossi, Liane M . Economically attractive route for the preparation of high quality magnetic nanoparticles by the thermal decomposition of iron(III) acetylacetonate. <strong>Nanotechnology (Bristol. Print),</strong> v. 28, p. 115603, 2017.
            <a href="http://dx.doi.org/10.1088/1361-6528/aa5ab0"><strong>Clique aqui</strong></a>
            
        </li>
    </ul>
    <ul type="disc">
        <li>
            GONÇALVES, RENATO V. ; Vono, Lucas L.R. ; WOJCIESZAK, ROBERT ; DIAS, CARLOS S.B. ; WENDER, HEBERTON ; TEIXEIRA-NETO, ERICO ; Rossi, Liane M. . Selective hydrogenation of CO 2 into CO on a highly dispersed nickel catalyst obtained by magnetron sputtering deposition: A step towards liquid fuels. Applied Catalysis <strong>B: Environmental (Print)</strong>, v. 209, p. 240-246, 2017.
            <a href="http://dx.doi.org/10.1016/j.apcatb.2017.02.081"><strong>Clique aqui</strong></a>
            
        </li>
    </ul>
    <ul type="disc">
        <li>
            FIORIO, JHONATAN L. ; L�PEZ, N�RIA ; Rossi, Liane M. . Gold-Ligand-Catalyzed Selective Hydrogenation of Alkynes into -Alkenes via H Heterolytic Activation by Frustrated Lewis Pairs. <strong>ACS Catalysis,</strong> v. 7, p. 2973-2980, 2017.
            <a href="http://dx.doi.org/10.1021/acscatal.6b03441"><strong>Clique aqui</strong></a>
            
        </li>
    </ul>
    <ul type="disc">
        <li>
            TEIXEIRA-NETO, A. A. ; GONÇALVES, R. V. ; RODELLA, C. B. ; ROSSI, L. M. ; TEIXEIRA-NETO, E. . Surface composition and structural changes on titanium oxide-supported AuPd nanoparticles during CO oxidation. <strong>Catalysis Science &amp; Technology,</strong> v. 7, p. 1679-1689, 2017.
            <a href="http://dx.doi.org/10.1039/c7cy00137a"><strong>Clique aqui</strong></a>
        </li>
    </ul>

    <ul type="disc">
        <li>
            Vono, Lucas L. R. ; DAMASCENO, CAMILA C. ; Matos, Jivaldo R. ; Jardim, Renato F. ; Landers, Richard ; Masunaga, Sueli H. ; Rossi, Liane M. . Separation technology meets green chemistry: development of magnetically recoverable catalyst supports containing silica, ceria, and titania.<strong> PURE AND APPLIED CHEMISTRY (ONLINE)</strong>, v. 0, p. 133-141, 2017.
            <a href="http://dx.doi.org/10.1515/pac-2017-0504"><strong>Clique aqui</strong></a>
        </li>
    </ul>
    <ul type="disc">
        <li>
            DA SILVA, FERNANDA PARRA ; FIORIO, JHONATAN LUIZ ; Rossi, Liane Marcia . Tuning the Catalytic Activity and Selectivity of Pd Nanoparticles Using Ligand-Modified Supports and Surfaces.<strong> ACS Omega</strong>, v. 2, p. 6014-6022, 2017.
            <a href="http://dx.doi.org/10.1021/acsomega.7b00836"><strong>Clique aqui</strong></a>
            
        </li>
    </ul>
    <ul type="disc">
        <li>
            Costa, Nat�lia J. S. ; Vono, Lucas L. R. ; WOJCIESZAK, ROBERT ; TEIXIERA-NETO, É�ICO ; Philippot, Karine ; Rossi, Liane M. . One-pot organometallic synthesis of alumina-embedded Pd nanoparticles.<strong> DALTON TRANSACTIONS,</strong> v. 46, p. 14318-14324, 2017.
            <a href="http://dx.doi.org/10.1039/c7dt02792c"><strong>Clique aqui</strong></a>
            
        </li>
    </ul>
    <ul type="disc">
        <li>
            GARCIA, MARCO A.S. ; IBRAHIM, MAHMOUD ; Costa, Jean C.S. ; Corio, Paola ; Gusevskaya, Elena V. ; DOS SANTOS, EDUARDO N. ; Philippot, Karine ; Rossi, Liane M. . Study of the influence of PPh 3 used as capping ligand or as reaction modifier for hydroformylation reaction involving Rh NPs as precatalyst.<strong> APPLIED CATALYSIS A-GENERAL</strong>, v. 548, p. 136-142, 2017.
            <a href="http://dx.doi.org/10.1016/j.apcata.2017.08.009"><strong>Clique aqui</strong></a>
            
        </li>
    </ul>
    <ul type="disc">
        <li>
            WOJCIESZAK, ROBERT ; FERRAZ, CAMILA P. ; SHA, JIN ; HOUDA, SARAH ; Rossi, Liane M. ; PAUL, S�BASTIEN . Advances in Base-Free Oxidation of Bio-Based Compounds on Supported Gold Catalysts. <strong>Catalysts,</strong> v. 7, p. 352, 2017.
            <a href="http://dx.doi.org/10.3390/catal7110352"><strong>Clique aqui</strong></a>
            
        </li>
    </ul>
    <ul type="disc">
        <li>
            FREDERICE, RAFAEL ; LENCIONE, DIEGO ; Gehlen, Marcelo H . Imaging the photoinduced charge injection in CdS/TiO nanoparticles by the sequential fluorescence mapping method. <strong>Methods and Applications in Fluorescence,</strong> v. 5, p. 014004, 2017.
            <a href="http://dx.doi.org/10.1088/2050-6120/aa5bed"><strong>Clique aqui</strong></a>

        </li>
    </ul>
    <ul type="disc">
        <li>
            LAUER, MILENA HELMER ; VRANKEN, CHARLOTTE ; DEEN, JOCHEM ; WAND, NATHANIEL ; FREDERICKX, WOUT ; VANDERLINDEN, WILLEM ; LEEN, VOLKER ; GEHLEN, MARCELO HENRIQUE ; HOFKENS, JOHAN ; NEELY, ROBERT KENNETH . Methyltransferase-directed covalent coupling of fluorophores to DNA.<strong> Chemical Science,</strong> v. xx, p. 1-8, 2017.
            <a href="http://dx.doi.org/10.1039/C6SC04229E"><strong>Clique aqui</strong></a>
            
        </li>
    </ul>
    <ul type="disc">
        <li>
            LINO, ALINE M. ; Gehlen, Marcelo H. . Styryl dye formation promoted by catalytic centers of piperazine bound to a silica surface traced by single molecule fluorescence microscopy<strong>. PHYSICAL CHEMISTRY CHEMICAL PHYSICS,</strong> v. 19, p. 20984-20990, 2017.
            <a href="http://dx.doi.org/10.1039/C7CP03437G"><strong>Clique aqui</strong></a>
            
        </li>
    </ul>
    <ul type="disc">
        <li>
            ABREU, FELIPE DI�GENES ; PAULO, TERCIO DE F. ; Gehlen, Marcelo H. ; ANDO, R�MULO A. ; LOPES, LUIZ G. F. ; GONDIM, ANA CL�UDIA S. ; VASCONCELOS, MAYRON A. ; TEIXEIRA, EDSON H. ; SOUSA, EDUARDO HENRIQUE SILVA ; DE CARVALHO, IDALINA MARIA MOREIRA . Aryl-Substituted Ruthenium(II) Complexes: A Strategy for Enhanced Photocleavage and Efficient DNA Binding.<strong> INORGANIC CHEMISTRY,</strong> v. 56, p. 9084-9096, 2017.
            <a href="http://dx.doi.org/10.1021/acs.inorgchem.7b01108"><strong>Clique aqui</strong></a>
            
        </li>
    </ul>
    <ul type="disc">
        <li>
            APARECIDA SABATINI, CAROLINA ; MASSUCATTO DOS SANTOS, DENIS ; MATOS DE OLIVEIRA DA SILVA, SABRINA ; HENRIQUE GEHLEN, MARCELO . Monitoring the Activity of Immobilized Lipase with Quinizarin Diester Fluoro-Chromogenic Probe.<strong> MOLECULES</strong>, v. 22, p. 2136, 2017.
            <a href="http://dx.doi.org/10.3390/molecules22122136"><strong>Clique aqui</strong></a>
        </li>
    </ul>
    <ul type="disc">
        <li>
            BARBOSA, C. D. E. S. ; DA LUZ, L. L. ; PAZ, F. A. ALMEIDA ; MALTA, O. L. ; Rodrigues, M. O. ; J�NIOR, S. A. ; FERREIRA, R. A. S. ; CARLOS, L. D. . Site-selective Eu( iii ) spectroscopy of highly efficient luminescent mixed-metal Pb( ii )/Eu( iii ) coordination polymers.<strong>RSC Advances: an international journal to further the chemical sciences</strong>, v. 7, p. 6093-6101, 2017.
            <a href="http://dx.doi.org/10.1039/c6ra27850g"><strong>Clique aqui</strong></a>

        </li>
    </ul>
    <ul type="disc">
        <li>
            MAURICIO, F.G.M. ; PRALON, A.Z. ; TALHAVINI, M. ; RODRIGUES, M.O. ; WEBER, I.T. . Identification of ANFO: Use of luminescent taggants in post-blast residues. <strong>Forensic Science International</strong>, v. 275, p. 8-13, 2017.
            <a href="http://dx.doi.org/10.1016/j.forsciint.2017.02.029"><strong>Clique aqui</strong></a>
            
        </li>
    </ul>
    <ul type="disc">
        <li>
            CALIL J�NIOR, MARCOS ; MELO, �TILA ; RODRIGUES, EMILLE ; SIGOLI, FERNANDO ; RODRIGUES, MARCELO . The Effect of Hydrothermal Treatment on the Morphologies and Optical Properties of Upconversion NaYF4:Ln3+ Crystals.<strong> JOURNAL OF THE BRAZILIAN CHEMICAL SOCIETY,</strong> v. 28, p. 1816-1821, 2017.
            <a href="http://dx.doi.org/10.21577/0103-5053.20170068"><strong>Clique aqui</strong></a>
            
        </li>
    </ul>
    <ul type="disc">
        <li>
            FERREIRA, Misael ; ASSUN��O, LAURA SARTORI ; SILVA, ADNY HENRIQUE ; FILIPPIN-MONTEIRO, FAB�OLA BRANCO ; CRECZYNSKI-PASA, T�NIA BEATRIZ ; S�, Marcus Mandolesi . Allylic isothiouronium salts: The discovery of a novel class of thiourea analogues with antitumor activity.<strong> European Journal of Medicinal Chemistry</strong>, v. 129, p. 151-158, 2017.
            <a href="http://dx.doi.org/10.1016/j.ejmech.2017.02.013"><strong>Clique aqui</strong></a>

        </li>
    </ul>
    <ul type="disc">
        <li>
            BORTOLUZZI, ADAILTON J. ; SILVEIRA, GUSTAVO P. ; S�, MARCUS M. . Crystal structure of 5- O -benzoyl-2,3- O -isopropylidene- D -ribono-1,4-lactone. Acta Crystallographica Section E Crystallographic Communications, v. 73, p. 407-409, 2017.
            <a href="http://dx.doi.org/10.1107/s2056989017002043"><strong>Clique aqui</strong></a>
            
        </li>
    </ul>
    <ul type="disc">
        <li>
            COSTIN, TA&amp;Iaacute;SSA A. ; DUTRA, LUIZ G. ; BORTOLUZZI, ADAILTON J. ; S�, MARCUS M. . Amine-mediated synthesis of amides from 1,3-dicarbonyl compounds through a domino diazo transfer/aminolysis process. <strong>TETRAHEDRON,</strong> v. 73, p. 4549-4559, 2017.
            <a href="http://dx.doi.org/10.1016/j.tet.2017.06.013"><strong>Clique aqui</strong></a>
            
        </li>
    </ul>
    <ul type="disc">
        <li>
            BATISTA, BRUNA G. ; LANA, DAIANE F. DALLA ; SILVEIRA, GUSTAVO P. ; S�, MARCUS M. ; FERREIRA, Misael ; RUSSO, THEO V. C. ; CANTO, R�MULO F. S. ; BARBOSA, FLAVIO A. R. ; BRAGA, ANT�NIO L. ; KAMINSKI, TA�S F. A. ; DE OLIVEIRA, LU�S F. S. ; MACHADO, MICHEL M. ; LOPES, WILLIAM ; VAINSTEIN, MARILENE H. ; TEIXEIRA, M�RIO L. ; ANDRADE, SAULO F. ; FUENTEFRIA, ALEXANDRE M. . Allylic Selenocyanates as New Agents to Combat Fusarium Species Involved with Human Infections. <strong>ChemistrySelect,</strong> v. 2, p. 11926-11932, 2017.
            <a href="http://dx.doi.org/10.1002/slct.201702338"><strong>Clique aqui</strong></a>
            
        </li>
    </ul>
    <ul type="disc">
        <li>
            XAVIER, DAIANE M. ; GOLDANI, BRUNA S. ; SEUS, NAT�LIA ; JACOB, RAQUEL G. ; Barcellos, Thiago ; Paix�o, M�rcio W. ; LUQUE, RAFAEL ; Alves, Diego . Sonochemistry in organocatalytic enamine-azide [3+2] cycloadditions: A rapid alternative for the synthesis of 1,2,3-triazoyl carboxamides. <strong>Ultrasonics Sonochemistry</strong>, v. 34, p. 107-114, 2017.
            <a href="http://dx.doi.org/10.1016/j.ultsonch.2016.05.007"><strong>Clique aqui</strong></a>

        </li>
    </ul>
    <ul type="disc">
        <li>
            CORREA, ARLENE GON�ALVES ; VIEIRA, LUCAS CAMPOS CURCINO ; MATSUO, BIANCA T ; GALL, MAYARA ; PAIXAO, MARCIO WEBER ; MARTELLI, LORENA S R . Asymmetric synthesis of new &#947;-butenolides via organocatalyzed epoxidation of chalcones. <strong>ORGANIC &amp; BIOMOLECULAR CHEMISTRY,</strong> v. 15, p. 6098-6013, 2017.
            <a href="http://dx.doi.org/10.1039/c7ob00165g"><strong>Clique aqui</strong></a>
            
        </li>
    </ul>
    <ul type="disc">
        <li>
            Zukerman-Schpector, Julio ; DALLASTA PEDROSO, SOFIA ; SOUSA MADUREIRA, LUCAS ; WEBER PAIX�O, M�RCIO ; ALI, AKBAR ; TIEKINK, EDWARD R. T. . 4-Benzyl-1-(4-nitrophenyl)-1 H -1,2,3-triazole: crystal structure and Hirshfeld analysis. <strong>ACTA CRYSTALLOGRAPHICA SECTION E: CRYSTALLOGRAPHIC COMMUNICATIONS,</strong> v. 73, p. 1716-1720, 2017.
            <a href="http://dx.doi.org/10.1107/s2056989017014748"><strong>Clique aqui</strong></a>
            
        </li>
    </ul>
    <ul type="disc">
        <li>
            JORGE, ERLEN ; LIMA, THIAGO DE MELO ; LIMA, CAROLINA ; MARCHINI, LUCAS ; CASTELBLANCO, WILLIAM NOVA ; Rivera, Daniel G. ; URQUIETA-GONZ�LEZ, ERNESTO ANTONIO ; VARMA, RAJENDER S ; PAIXAO, MARCIO WEBER . Metal-exchanged magnetic &#946; zeolites: valorization of lignocellulosic biomass-derived compounds to platform chemicals. <strong>GREEN CHEMISTRY</strong>, v. 19, p. 3856-3868, 2017.
            <a href="http://dx.doi.org/10.1039/c7gc01178d"><strong>Clique aqui</strong></a>
            
        </li>
    </ul>
    <ul type="disc">
        <li>
            DOS SANTOS, DEBORAH A. ; Deobald, Anna Maria ; CORNELIO, VIVIAN E. ; �VILA, ROBERTA M.D. ; CORNEA, RENATA C. ; BERNASCONI, GILBERTO C.R. ; Paix�o, Marcio W. ; VIEIRA, PAULO C. ; Corrêa, Arlene G. . Asymmetric synthesis and evaluation of epoxy-α-acyloxycarboxamides as selective inhibitors of cathepsin L. <strong>BIOORGANIC &amp; MEDICINAL CHEMISTRY</strong>, v. 25, p. 4620-4627, 2017.
            <a href="http://dx.doi.org/10.1016/j.bmc.2017.06.048"><strong>Clique aqui</strong></a>
            
        </li>
    </ul>
    <ul type="disc">
        <li>
            CASAGRANDE, OSVALDO DE LAZARO; PINHEIRO, ADRIANA ; MORAES, SABRINA ; Roisnel, Thierry ; KIRILLOV, EVGUENI ; CARPENTIER, JEAN-FRANCOIS . Synthesis and Structural Characterization of Zirconium Complexes Supported by Tridentate Pyrrolide-Imino Ligands with Pendant N-, O- and S-donor Groups and Their Application in Ethylene Polymerization.<strong>NEW JOURNAL OF CHEMISTRY,</strong> v. 42, p. 1477-1483, 2017.
            <a href="http://dx.doi.org/10.1039/c7nj04074a"><strong>Clique aqui</strong></a>
            
        </li>
    </ul>
    <ul type="disc">
        <li>
            DRESCH, LUCIELLE C. ; JUNGES, CARLOS H. ; Casagrande, Osvaldo de L. ; STIELER, RAFAEL . Nickel complexes supported by selenium-based tridentate ligands and their use as effective catalyst systems for ethylene dimerisation. <strong>JOURNAL OF ORGANOMETALLIC CHEMISTRY,</strong> v. 856, p. 34-40, 2017.
            <a href="http://dx.doi.org/10.1016/j.jorganchem.2017.12.025"><strong>Clique aqui</strong></a>
            
        </li>
    </ul>
    <ul type="disc">
        <li>
            DA CRUZ, K�TIA Z. C ; CASAGRANDE, A. C. A. ; CASAGRANDE JUNIOR, O. L. . High-density polyethylene/expanded graphite nanocomposites produced by polymerization-filling technique using an industrial heterogeneous catalyst.<strong> JOURNAL OF POLYMER SCIENCE PART A-POLYMER CHEMISTRY</strong>, v. 55, p. 1260-1267, 2017.
            <a href="http://dx.doi.org/10.1002/pola.28493"><strong>Clique aqui</strong></a>
        </li>
    </ul>

    <ul type="disc">
        <li>
            MITTERSTEINER, MATEUS ; MACHADO, TAYANI ; DE JESUS, PAULO CESAR ; BRONDANI, PATR�CIA ; SCHARF, DILAMARA ; WENDHAUSEN JR., RENATO . Easy and Simple SiO2 Immobilization of Lipozyme CaLB-L: Its Use as a Catalyst in Acylation Reactions and Comparison with Other Lipases.<strong>JOURNAL OF THE BRAZILIAN CHEMICAL SOCIETY,</strong> v. 28, p. 1185-1192, 2017.
            <a href="http://dx.doi.org/10.21577/0103-5053.20160277"><strong>Clique aqui</strong></a>
        </li>
    </ul>
    <ul type="disc">
        <li>
            MON�ALVES, MATIAS ; ZANOTTO, GABRIEL M. ; TOLDO, JOSENE M. ; Rampon, Daniel S. ; Schneider, Paulo H. ; Gon�alves, Paulo F. B. ; Rodembusch, Fabiano S. ; SILVEIRA, CLAUDIO C. . Dipolar vinyl sulfur fluorescent dyes. Synthesis and photophysics of sulfide, sulfoxide and sulfone based D-&#960;-A compounds. <strong>RSC Advances: an international journal to further the chemical sciences</strong>,v. 7, p. 8832-8842, 2017.
            <a href="http://dx.doi.org/10.1039/c6ra27989a"><strong>Clique aqui</strong></a>

        </li>
    </ul>
    <ul type="disc">
        <li>
            SOUSA, FERNANDA SEVERO SABEDRA ; SEUS, NAT�LIA ; Alves, Diego ; SALLES, HELENA DOMINGUES ; Schneider, Paulo H. ; Savegnago, Lucielli ; CASTRO, MICHELI . Evaluation of Se-phenyl-thiazolidine-4-carboselenoate protective activity against oxidative and behavioral stress in the maniac model induced by ouabain in male rats. <strong>NEUROSCIENCE LETTERS</strong>, v. 651, p. 182-187, 2017.
            <a href="http://dx.doi.org/10.1016/j.neulet.2017.04.030"><strong>Clique aqui</strong></a>
            
        </li>
    </ul>
    <ul type="disc">
        <li>
            XAVIER, MAUR�CIO C.D.F. ; GOLDANI, BRUNA ; SCHUMACHER, RICARDO F. ; PERIN, GELSON ; Schneider, Paulo Henrique ; Alves, Diego . Silver-catalyzed direct selenylation of terminal alkynes through C H bond functionalization.<strong> Molecular Catalysis,</strong> v. 427, p. 73-79, 2017.
            <a href="http://dx.doi.org/10.1016/j.molcata.2016.11.033"><strong>Clique aqui</strong></a>
            
        </li>
    </ul>
    <ul type="disc">
        <li>
            NOBRE, PATRICK C. ; VARGAS, HENRIQUE A. ; JACOBY, CAROLINE G. ; Schneider, Paulo H. ; CASARIL, ANGELA M. ; Savegnago, Lucielli ; SCHUMACHER, RICARDO F. ; LENARD�O, EDER J. ; �VILA, DAIANA S. ; RODRIGUES JUNIOR, LUIZ B.L. ; PERIN, GELSON . Synthesis of enantiomerically pure glycerol derivatives containing an organochalcogen unit: in vitro and in vivo antioxidant activity. <strong>Arabian Journal of Chemistry</strong>, v. s, p. n, 2017.
            <a href="http://dx.doi.org/10.1016/j.arabjc.2017.08.007"><strong>Clique aqui</strong></a>
            
        </li>
    </ul>
    <ul type="disc">
        <li>
            Schneider, Paulo Henrique; BACH, MARIANA FERRARI ; GRIEBELER, CASSIANA HERZER ; JACOBY, CAROLINE GROSS . Design of a New Chiral Ionic Liquids System for the Enantioselective Addition of Diethylzinc to Aldehydes. <strong>EUROPEAN JOURNAL OF ORGANIC CHEMISTRY</strong>, v. 46, p. 6997-7004, 2017.
            <a href="http://dx.doi.org/10.1002/ejoc.201701426"><strong>Clique aqui</strong></a>
            
        </li>
    </ul>
    <ul type="disc">
        <li>
            RODRIGUES, THENNER S. ; DA SILVA, ANDERSON G.M. ; DE OLIVEIRA, LUCAS C. ; DA SILVA, ADALBERTO M. ; TEIXEIRA, R�BSON R. ; Camargo, Pedro H.C. . Cu2O spheres as an efficient source of catalytic Cu(I) species for performing azide-alkyne click reactions. <strong>Tetrahedron Letters,</strong> v. 58, p. 590-595, 2017.
            <a href="http://dx.doi.org/10.1016/j.tetlet.2017.01.005"><strong>Clique aqui</strong></a>
            
        </li>
    </ul>
    <ul type="disc">
        <li>
            PAPA, LETIZIA ; DE FREITAS, ISABEL ; GEONMONOND, RAFAEL DOS SANTOS ; AQUINO, CAROLINE ; PIERETTI, JOANA ; DOMINGUES, SERGIO ; ANDO, R�MULO AUGUSTO ; CAMARGO, PEDRO . Supports Matter: Unraveling the Role of Charge-Transfer over the Plasmonic Catalytic Activity of Silver Nanoparticles. <strong>Journal of Materials Chemistry A,</strong> v. 5, p. 11720-11729, 2017.
            <a href="http://dx.doi.org/10.1039/c6ta10122d"><strong>Clique aqui</strong></a>
            
        </li>
    </ul>
    <ul type="disc">
        <li>
            DA SILVA, ANDERSON ; RODRIGUES, THENNER ; HAIGH, SARAH J ; CAMARGO, PEDRO . Galvanic Replacement Reaction: Recent Developments for Engineering Metal Nanostructures towards Catalytic Applications. <strong>CHEMICAL COMMUNICATIONS</strong>, v. 53, p. 7135, 2017.
            <a href="http://dx.doi.org/10.1039/c7cc02352a"><strong>Clique aqui</strong></a>
            
        </li>
    </ul>
    <ul type="disc">
        <li>
            WANG, JIALE ; DE FREITAS, ISABEL ; ALVES, TIAGO ; ANDO, ROMULO A. ; FANG, ZEBO ; CAMARGO, PEDRO . On the Effect of Native SiO2 on Si over the SPR-mediated Photocatalytic Activities of Au and Ag Nanoparticles. <strong>CHEMISTRY-A EUROPEAN JOURNAL</strong>, v. 23, p. 7185, 2017.
            <a href="http://dx.doi.org/10.1002/chem.201700651"><strong>Clique aqui</strong></a></li>
        </ul>	
    


<ul type="disc">
    <li>
        DA SILVA, ANDERSON G. M. ; RODRIGUES, THENNER S. ; PARUSSULO, ANDRÉ L. A. ; CANDIDO, EDUARDO G. ; GEONMONOND, RAFAEL S. ; BRITO, HERMI F. ; TOMA, HENRIQUE E. ; Camargo, Pedro H. C. . Controlled Synthesis of Nanomaterials at the Undergraduate Laboratory: Cu(OH) 2 and CuO Nanowires. <strong>JOURNAL OF CHEMICAL EDUCATION,</strong> v. 94, p. 743-750, 2017.
        <a href="http://dx.doi.org/10.1021/acs.jchemed.6b00185"><strong>Clique aqui</strong></a>
        
    </li>
</ul>
<ul type="disc">
    <li>
        Camargo, Pedro H. C. . I. David Brown: The chemical bond in inorganic chemistry: the bond valence model, 2nd ed. <strong>JOURNAL OF MATERIALS SCIENCE,</strong> p. 9959, 2017.
        <a href="http://dx.doi.org/10.1007/s10853-017-1215-2"><strong>Clique aqui</strong></a>
        
    </li>
</ul>
<ul type="disc">
    <li>
        SILVA, VALMIR B. ; RODRIGUES, THENNER S. ; Camargo, Pedro H. C. ; ORTH, ELISA S. . Detoxification of organophosphates using imidazole-coated Ag, Au and AgAu nanoparticles. <strong>RSC Advances,</strong> v. 7, p. 40711-40719, 2017.
        <a href="http://dx.doi.org/10.1039/c7ra07059d"><strong>Clique aqui</strong></a>
        
    </li>
</ul>
<ul type="disc">
    <li>
        DA SILVA, ALISSON H. M. ; RODRIGUES, THENNER S. ; DA SILVA, ANDERSON G. M. ; Camargo, Pedro H. C. ; GOMES, JANAINA F. ; ASSAF, JOS� M. . Systematic investigation of the effect of oxygen mobility on CO oxidation over AgPt nanoshells supported on CeO2, TiO2 and Al2O3. <strong>JOURNAL OF MATERIALS SCIENCE (DORDRECHT. ONLINE),</strong> v. 52, p. 13764-13778, 2017.
        <a href="http://dx.doi.org/10.1007/s10853-017-1481-z"><strong>Clique aqui</strong></a>
        
    </li>
</ul>
<ul type="disc">
    <li>
        LIMA, D�BORA R. ; JIANG, NING ; LIU, XIN ; WANG, JIALE ; VULCANI, VALCINIR A. S. ; MARTINS, ALESSANDRO ; MACHADO, DOUGLAS S. ; LANDERS, RICHARD ; Camargo, Pedro H. C. ; PANCOTTI, ALEXANDRE . Employing Calcination as a Facile Strategy to Reduce the Cytotoxicity in CoFe 2 O 4 and NiFe 2 O 4 Nanoparticles. <strong>ACS Applied Materials &amp; Interfaces</strong>, v. 9, p. 39830-39838, 2017.
        <a href="http://dx.doi.org/10.1021/acsami.7b13103"><strong>Clique aqui</strong></a>
    </li>
</ul>
<ul type="disc">
    <li>
        WANG, Y C ; SLATER, T J A ; RODRIGUES, T S ; CAMARGO, P H C ; HAIGH, S J . Automated quantification of morphology and chemistry from STEM data of individual nanoparticles. JOURNAL OF PHYSICS.<strong> CONFERENCE SERIES (PRINT)</strong>, v. 902, p. 012018, 2017.
        <a href="http://dx.doi.org/10.1088/1742-6596/902/1/012018"><strong>Clique aqui</strong></a>
    </li>
</ul>
<ul type="disc">
    <li>
        DA SILVA, FILIPE LINS ; DO NASCIMENTO, JEILMA RODRIGUES ; DE MELO, LUCAS NAT� ; DE FREITAS, JOS� ANDERSON SILVA ; BORTOLUZZI, JANA�NA HEBERLE ; MENEGHETTI, SIMONI MARGARETI PLENTZ . Study of correlations between composition and physicochemical properties during methylic and ethylic biodiesel synthesis. <strong>Industrial Crops and Products (Print)</strong>, v. 95, p. 18-26, 2017.
        <a href="http://dx.doi.org/10.1016/j.indcrop.2016.09.053"><strong>Clique aqui</strong></a>

    </li>
</ul>
<ul type="disc">
    <li>
        NUNES, RAFAEL S. ; ALTINO, FELYPPE M. ; Meneghetti, Mario R. ; Meneghetti, Simoni M.P. . New mechanistic approaches for fatty acid methyl ester production reactions in the presence of Sn(IV) catalysts. <strong>CATALYSIS TODAY</strong>, v. 289, p. 121-126, 2017.
        <a href="http://dx.doi.org/10.1016/j.cattod.2016.09.016"><strong>Clique aqui</strong></a>
        
    </li>
</ul>
<ul type="disc">
    <li>
        DA SILVA, M�NICA ARA�JO ; DOS SANTOS, ANDERSON SELTON SILVA ; DOS SANTOS, THATIANE VER�SSIMO ; MENEGHETTI, Mario Roberto ; MENEGHETTI, SIMONI MARGARETI PLENTZ . Organotin( ) compounds with high catalytic activities and selectivities in the glycerolysis of triacylglycerides. <strong>Catalysis Science &amp; Technology,</strong> v. 7, p. 5750-5757, 2017.
        <a href="http://dx.doi.org/10.1039/C7CY01559C"><strong>Clique aqui</strong></a>
        
    </li>
</ul>
<ul type="disc">
    <li>
        BARBOSA, ANA SORAYA LIMA ; DE SIQUEIRA GUEDES, J�SSICA ; DA SILVA, DOUGLAS ROZENDO ; MENEGHETTI, SIMONI MARGARETI PLENTZ ; MENEGHETTI, Mario Roberto ; DA SILVA, AMANDA EVELYN ; DE ARAUJO, MORGANA VITAL ; ALEXANDRE-MOREIRA, MAGNA SUZANA ; DE AQUINO, THIAGO MENDON�A ; DE SIQUEIRA JUNIOR, JOS� PINTO ; DE ARA�JO, RODRIGO SANTOS AQUINO ; DA CRUZ, RYLDENE MARQUES DUARTE ; MENDONÇA-JUNIOR, FRANCISCO JAIME BEZERRA . Synthesis and evaluation of the antibiotic and adjuvant antibiotic potential of organotin(IV) derivatives.<strong> JOURNAL OF INORGANIC BIOCHEMISTRY,</strong> v. 180, p. 80-88, 2017.
        <a href="http://dx.doi.org/10.1016/j.jinorgbio.2017.12.004"><strong>Clique aqui</strong></a>
        
    </li>
</ul>
<ul type="disc">
    <li>
        ABRANTES COSTA, D�BORA MARIA ; FIGUEIREDO COSTA, MARIANA AMALIA ; GUIMAR�ES, SAMUEL LEITE ; COITINHO, JULIANA BARBOSA ; G�MEZ, STEFANYA VEL�SQUEZ ; ANT�NIO DA SILVA BRAND�O, TIAGO ; PINTO NAGEM, RONALDO ALVES . A combined approach for enhancing the stability of recombinant cis-dihydrodiol naphthalene dehydrogenase from Pseudomonas putida G7 allowed for the structural and kinetic characterization of the enzyme. <strong>Protein Expression and Purification (Print)</strong>, v. 132, p. 50-59, 2017.
        <a href="http://dx.doi.org/10.1016/j.pep.2017.01.005"><strong>Clique aqui</strong></a>
    </li>
</ul>
<ul type="disc">
    <li>
        Ven�ncio, Mateus F. ; DOCTOROVICH, FABIO ; Rocha, Willian R. . Solvation and Proton-Coupled Electron Transfer Reduction Potential of 2 NO - to 1 HNO in Aqueous Solution: A Theoretical Investigation. <strong>JOURNAL OF PHYSICAL CHEMISTRY B,</strong> v. 121, p. 6618-6625, 2017.
        <a href="http://dx.doi.org/10.1021/acs.jpcb.7b03552"><strong>Clique aqui</strong></a>

    </li>
</ul>
<ul type="disc">
    <li>
        OLIVEIRA, ALEXANDRE A. ; PERDIG�O, GABRIELE M. C. ; RODRIGUES, LUANA E. ; da Silva, Jeferson G. ; SOUZA-FAGUNDES, ELAINE M. ; TAKAHASHI, JACQUELINE A. ; Rocha, Willian R. ; Beraldo, Heloisa . Cytotoxic and antimicrobial effects of indium( iii ) complexes with 2-acetylpyridine-derived thiosemicarbazones. <strong>DALTON TRANSACTIONS</strong>, v. 46, p. 918-932, 2017.
        <a href="http://dx.doi.org/10.1039/c6dt03657k"><strong>Clique aqui</strong></a>
        
    </li>
</ul>
<ul type="disc">
    <li>
        DOS SANTOS, H�LIO F. ; CHAGAS, MARCELO A. ; DE SOUZA, LEONARDO A. ; Rocha, Willian R. ; DE ALMEIDA, MAURO V. ; Anconi, Cleber P. A. ; De Almeida, Wagner B. . Water Solvent Effect on Theoretical Evaluation of 1 H NMR Chemical Shifts: o -Methyl-Inositol Isomer.<strong> JOURNAL OF PHYSICAL CHEMISTRY A</strong>, v. 121, p. 2839-2846, 2017.
        <a href="http://dx.doi.org/10.1021/acs.jpca.7b01067"><strong>Clique aqui</strong></a>
        
    </li>
</ul>
<ul type="disc">
    <li>
        SUAREZ, SEBASTIAN A. ; MU�OZ, MARTINA ; ALVAREZ, LUCIA ; VENANCIO, MATEUS F. ; ROCHA, WILLIAN ; BIKIEL, DAMIAN E. ; MARTI, MARCELO A. ; DOCTOROVICH, FABIO . HNO is produced by the reaction of NO with thiols. <strong>Journal of the American Chemical Society</strong>, v. XX, p. jacs.7b06968, 2017.
        <a href="http://dx.doi.org/10.1021/jacs.7b06968"><strong>Clique aqui</strong></a>
        
    </li>
</ul>
<ul type="disc">
    <li>
        REIS, NATALIA V. ; BARROS, WDESON P. ; OLIVEIRA, WILLIAN X. C. ; PEREIRA, CYNTHIA L. M. ; Rocha, Willian R. ; PINHEIRO, CARLOS B. ; LLORET, FRANCESC ; JULVE, MIGUEL ; STUMPF, HUMBERTO O. . Crystal Structure and Magnetic Properties of an Oxamato-Bridged Heterobimetallic Tetranuclear [Ni Cu ] Complex of the Rack Type. <strong>EUROPEAN JOURNAL OF INORGANIC CHEMISTRY</strong>, v. XX, p. XX, 2017.
        <a href="http://dx.doi.org/10.1002/ejic.201700821"><strong>Clique aqui</strong></a>
        
    </li>
</ul>
<ul type="disc">
    <li>

        BIAJOLI, ANDR� F.P. ; PERINGER, FERNANDO ; MONTEIRO, Adriano L. . Pd(OAc)2/dppp, an efficient catalytic system for the oxidative esterification of benzaldehyde using organic halides as oxidants. <strong>Catalysis Communications (Print),</strong> v. 89, p. 48-51, 2017.
        <a href="http://dx.doi.org/10.1016/j.catcom.2016.10.015"><strong>Clique aqui</strong></a>

    </li>
</ul>
<ul type="disc">
    <li>
        MONTEIRO, Adriano L.; FURLAN, MAYSA ; ZIANI SUAREZ, PAULO ANSELMO . Sistema Nacional de P?s-Gradua??o e a ?rea de Qu?mica na CAPES. <strong>QUIMICA NOVA,</strong> v. 40, p. 618-625, 2017.
        <a href="http://dx.doi.org/10.21577/0100-4042.20170079"><strong>Clique aqui</strong></a>

    </li>
</ul>
<ul type="disc">
    <li>
        MARTINS, GUILHERME ; DOS SANTOS, MARCELO ; RODRIGUES, MARCUS ; SUCUPIRA, RENATA ; MENEGHETTI, LUISA ; Monteiro, Adriano ; SUAREZ, PAULO . Cellulose Oxidation and the Use of Carboxyl Cellulose Metal Complexes in Heterogeneous Catalytic Systems to Promote Suzuki-Miyaura Coupling and C-O Bond Formation Reaction.<strong> JOURNAL OF THE BRAZILIAN CHEMICAL SOCIETY,</strong> v. 28, p. 2064-2072, 2017.
        <a href="http://dx.doi.org/10.21577/0103-5053.20170051"><strong>Clique aqui</strong></a>
    </li>
</ul>
<ul type="disc">
    <li>
        CLAUDINO, THIAGO S. ; SCHOLTEN, J. D. ; Monteiro, Adriano L . Selective Pd-catalyzed hydrogenation of 3,3-diphenylallyl alcohol: Efficient synthesis of 3,3-diarylpropylamine drugs diisopromine and feniprane. <strong>CATALYSIS COMMUNICATIONS,</strong> v. 102, p. 53-56, 2017.
        <a href="http://dx.doi.org/10.1016/j.catcom.2017.08.025"><strong>Clique aqui</strong></a>
    </li>
</ul>
<ul type="disc">
    <li>
        ROCHA, MANUELA S. T. ; RAFIQUE, JAMAL ; SABA, SUMBAL ; Azeredo, Juliano B. ; BACK, DAVI ; Godoi, Marcelo ; Braga, Antonio L. . Regioselective hydrothiolation of terminal acetylene catalyzed by magnetite (Fe 3 O 4 ) nanoparticles. <strong>Synthetic Communications</strong>, v. 47, p. 291-298, 2017.
        <a href="http://dx.doi.org/10.1080/00397911.2016.1262421"><strong>Clique aqui</strong></a>

    </li>
</ul>
<ul type="disc">
    <li>
        HO, PETER C. ; RAFIQUE, JAMAL ; LEE, JIWON ; LEE, LUCIA M. ; JENKINS, HILARY A. ; BRITTEN, JAMES F. ; Braga, Antonio L. ; VARGAS-BACA, IGNACIO . Synthesis and structural characterisation of the aggregates of benzo-1,2-chalcogenazole 2-oxides.<strong> DALTON TRANSACTIONS</strong>, v. 46, p. 6570-6579, 2017.
        <a href="http://dx.doi.org/10.1039/c7dt00612h"><strong>Clique aqui</strong></a>
        
    </li>
</ul>
<ul type="disc">
    <li>
        RAFIQUE, JAMAL ; SABA, SUMBAL ; SCHNEIDER, ALEX R. ; FRANCO, MARCELO S. ; SILVA, SYMARA M. ; Braga, Antonio L. . Metal- and Solvent-Free Approach to Access 3-Se/S-Chromones from the Cyclization of Enaminones in the Presence of Dichalcogenides Catalyzed by KIO 3.<strong> ACS Omega,</strong> v. 2, p. 2280-2290, 2017.
        <a href="http://dx.doi.org/10.1021/acsomega.7b00445"><strong>Clique aqui</strong></a>
        
    </li>
</ul>
<ul type="disc">
    <li>
        SABA, SUMBAL ; BOTTESELLE, GIANCARLO ; Godoi, Marcelo ; FRIZON, TIAGO ; Galetto, Fábio ; RAFIQUE, JAMAL ; Braga, Antonio . Copper-Catalyzed Synthesis of Unsymmetrical Diorganyl Chalcogenides (Te/Se/S) from Boronic Acids under Solvent-Free Conditions.<strong> MOLECULES</strong>, v. 22, p. 1367, 2017.
        <a href="http://dx.doi.org/10.3390/molecules22081367"><strong>Clique aqui</strong></a>
    </li>
</ul>
<ul type="disc">
    <li>
        Braga, Antonio Luiz; SILVA, LAIS T. ; Azeredo, Juliano B. ; SABA, SUMBAL ; RAFIQUE, JAMAL ; BORTOLUZZI, ADAILTON J. . Solvent- and metal-free chalcogenation of bicyclic arenes using I2/DMSO as non-metallic catalytic system. <strong>EUROPEAN JOURNAL OF ORGANIC CHEMISTRY,</strong> v. 32, p. 4740-4748, 2017.
        <a href="http://dx.doi.org/10.1002/ejoc.201700744"><strong>Clique aqui</strong></a>
        
    </li>
</ul>
<ul type="disc">
    <li>
        BATISTA, BRUNA G. ; LANA, DAIANE F. DALLA ; SILVEIRA, GUSTAVO P. ; S�, MARCUS M. ; FERREIRA, MISAEL ; RUSSO, THEO V. C. ; CANTO, R�MULO F. S. ; BARBOSA, FLAVIO A. R. ; BRAGA, ANT�NIO L. ; KAMINSKI, TA�S F. A. ; DE OLIVEIRA, LU�S F. S. ; MACHADO, MICHEL M. ; LOPES, WILLIAM ; VAINSTEIN, MARILENE H. ; TEIXEIRA, M�RIO L. ; ANDRADE, SAULO F. ; FUENTEFRIA, ALEXANDRE M. . Allylic Selenocyanates as New Agents to Combat Fusarium Species Involved with Human Infections. <strong>ChemistrySelect,</strong> v. 2, p. 11926-11932, 2017.
        <a href="http://dx.doi.org/10.1002/slct.201702338"><strong>Clique aqui</strong></a>
        
    </li>
</ul>

<ul type="disc">
    <li>
        SANTOS, ALEXANDRA G. ; BAILEY, GWENDOLYN A ; NICOLAU DOS SANTOS, EDUARDO ; FOGG, DERYN ELIZABETH . Overcoming Catalyst Decomposition in Acrylate Metathesis: Polyphenol Resins as Enabling Agents for PCy3-Stabilized Metathesis Catalysts. <strong>ACS Catalysis,</strong> v. 1, p. 1-10, 2017.
        <a href="http://dx.doi.org/10.1021/acscatal.6b03557"><strong>Clique aqui</strong></a>

    </li>
</ul>
<ul type="disc">
    <li>
        DOS SANTOS, EDUARDO N.; GRANATO, ARTUR V. ; SANTOS, ALEXANDRA G. . p-cymene as a solvent for olefin metathesis: matching efficiency and sustainability. <strong>ChemSusChem,</strong> v. 10, p. 1832-1837, 2017.
        <a href="http://dx.doi.org/10.1002/cssc.201700116"><strong>Clique aqui</strong></a>
        
    </li>
</ul>
<ul type="disc">
    <li>
        BERNARDO-GUSM�O, KATIA ; PERGHER, SIBELE B. C. ; DOS SANTOS, EDUARDO N. . Um panorama da Cat�lise no Brasil nos �ltimos 40 anos. <strong>QUIMICA NOVA,</strong> v. 40, p. 650-655, 2017.
        <a href="http://dx.doi.org/10.21577/0100-4042.20170083"><strong>Clique aqui</strong></a>
        
    </li>
</ul>
<ul type="disc">
    <li>
        GARCIA, MARCO A.S. ; IBRAHIM, MAHMOUD ; COSTA, JEAN C.S. ; CORIO, PAOLA ; Gusevskaya, Elena V. ; DOS SANTOS, EDUARDO N. ; PHILIPPOT, KARINE ; ROSSI, LIANE M. . Study of the influence of PPh 3 used as capping ligand or as reaction modifier for hydroformylation reaction involving Rh NPs as precatalyst. <strong>APPLIED CATALYSIS A-GENERAL</strong>, v. 548, p. 136-142, 2017.
        <a href="http://dx.doi.org/10.1016/j.apcata.2017.08.009"><strong>Clique aqui</strong></a>
    </li>
</ul>

<ul type="disc">
    <li>
        FRIEDRICH, L. C. ; ZANTA, C. L. P. S. ; MACHULECK JR, A. ; QUINA, F. H. . Estudo mecan�stico das rea��es Fenton e cupro-Fenton por an�lise voltam�trica in situ. <strong>QUIMICA NOVA,</strong> v. 40, p. 769-773, 2017.
        <a href="http://dx.doi.org/10.21577/0100-4042.20170065"><strong>Clique aqui</strong></a>

    </li>
</ul>
<ul type="disc">
    <li>
        Freitas, Adilson A. ; DA SILVA, CASSIO PACHECO ; SILVA, G. T. M. ; Ma�anita, Ant�nio L. ; Quina, Frank H. . From vine to wine: photophysics of a pyranoflavylium analog of red wine pyranoanthocyanins. <strong>PURE AND APPLIED CHEMISTRY (ONLINE),</strong> v. 89, p. 1761-1767, 2017.
        <a href="http://dx.doi.org/10.1515/pac-2017-0411"><strong>Clique aqui</strong></a>
        
    </li>
</ul>
<ul type="disc">
    <li>
        GEROLA, ADRIANA P. ; COSTA, PAULO F.A. ; Nome, Faruk ; QUINA, FRANK . Micellization and adsorption of zwitterionic surfactants at the air/water interface. <strong>CURRENT OPINION IN COLLOID &amp; INTERFACE SCIENCE,</strong> v. 32, p. 48-56, 2017.
        <a href="http://dx.doi.org/10.1016/j.cocis.2017.09.005"><strong>Clique aqui</strong></a>

    </li>
</ul>
<ul type="disc">
    <li>
        GEROLA, ADRIANA P. ; COSTA, PAULO F.A. ; QUINA, F. H. ; Fiedler, Haidi D. ; NOME, F . Zwitterionic Surfactants in Ion Binding and Catalysis. <strong>CURRENT OPINION IN COLLOID &amp; INTERFACE SCIENCE</strong>, v. 32, p. 39-47, 2017.
        <a href="http://dx.doi.org/10.1016/j.cocis.2017.10.002"><strong>Clique aqui</strong></a>
        
    </li>
</ul>
<ul type="disc">
    <li>
        RODRIGUES, ANA CLARA BELTRAN ; MARIZ, IN�S DE F�TIMA AFONSO ; MA�OAS, ERMELINDA MARIA SENGO ; TONELLI, RENATA ROSITO ; MARTINHO, JOS� MANUEL GASPAR ; QUINA, FRANK HERBERT ; BASTOS, ERICK LEITE . Bioinspired water-soluble two-photon fluorophores.<strong> DYES AND PIGMENTS,</strong> v. 150, p. 105-111, 2017.
        <a href="http://dx.doi.org/10.1016/j.dyepig.2017.11.020"><strong>Clique aqui</strong></a>
    </li>
</ul>
<ul type="disc">
    <li>
        Souza, Bruno S. ; MORA, JOSE R. ; WANDERLIND, EDUARDO H. ; CLEMENTIN, ROSILENE M. ; GESSER, JOSE C. ; Fiedler, Haidi D. ; NOME, Faruk ; MENGER, FREDRIC M. . Transforming a Stable Amide into a Highly Reactive One: Capturing the Essence of Enzymatic Catalysis. <strong>Angewandte Chemie (International ed. Print),</strong> v. 56, p. 1-5, 2017.
        <a href="http://dx.doi.org/10.1002/anie.201701306"><strong>Clique aqui</strong></a>
    </li>
</ul>
<ul type="disc">
    <li>
        GEROLA, ADRIANA P. ; WANDERLIND, EDUARDO H. ; GOMES, YASMIN S. ; GIUSTI, LUCIANO A. ; GARC�A-R�O, LUIS ; NOME, REN� A. ; KIRBY, ANTHONY J. ; Fiedler, Haidi D. ; NOME, Faruk . Supramolecular Polymer/Surfactant Complexes as Catalysts for Phosphate Transfer Reactions. <strong>ACS Catalysis</strong>, v. 7, p. 2230-2239, 2017.
        <a href="http://dx.doi.org/10.1021/acscatal.7b00097"><strong>Clique aqui</strong></a>

    </li>
</ul>
<ul type="disc">
    <li>
        ALMERINDO, GIZELLE ; GABORIM, ANIKA ; NICOLAZI, LUCAS ; Idrees, Muhammad ; NOME, Faruk ; FIEDLER, HAIDI ; NOME, RENE . Confocal Fluorescence Microscopy and Kinetics of the Cr3+-Chromate Ion Oxidation Equilibria at the Solid Liquid Interface. <strong>Journal of the Brazilian Chemical Society (Impresso),</strong> v. 28, p. 1-7, 2017.
        <a href="http://dx.doi.org/10.21577/0103-5053.20170015"><strong>Clique aqui</strong></a>
    </li>
</ul>
<ul type="disc">
    <li>
        GEROLA, ADRIANA P. ; COSTA, PAULO F.A. ; Quina, Frank H. ; Fiedler, Haidi D. ; NOME, Faruk . Zwitterionic Surfactants in Ion Binding and Catalysis. <strong>CURRENT OPINION IN COLLOID &amp; INTERFACE SCIENCE,</strong> v. 32, p. 39-47, 2017.
        <a href="http://dx.doi.org/10.1016/j.cocis.2017.10.002"><strong>Clique aqui</strong></a>
    </li>
</ul>
<ul type="disc">
    <li>
        ZANATTA, MARCILEIA ; DOS SANTOS, FRANCISCO P. ; BIEHL, CRISTINA ; MARIN, GRACIANE ; EBELING, GUNTER ; Netz, Paulo A. ; Dupont, Jairton . Organocatalytic Imidazolium Ionic Liquids H/D Exchange Catalysts. <strong>JOURNAL OF ORGANIC CHEMISTRY,</strong> v. 82, p. 2622-2629, 2017.
        <a href="http://dx.doi.org/10.1021/acs.joc.6b03029"><strong>Clique aqui</strong></a>

    </li>
</ul>
<ul type="disc">
    <li>
        WEILHARD, ANDREAS ; ABARCA, GABRIEL ; VISCARDI, JANINE ; Prechtl, Martin H. G. ; Scholten, Jackson D. ; BERNARDI, FABIANO ; BAPTISTA, DANIEL L. ; Dupont, Jairton . Challenging Thermodynamics: Hydrogenation of Benzene to 1,3-Cyclohexadiene by Ru@Pt Nanoparticles. <strong>ChemCatChem,</strong> v. 9, p. 204-211, 2017.
        <a href="http://dx.doi.org/10.1002/cctc.201601196"><strong>Clique aqui</strong></a>
        
    </li>
</ul>
<ul type="disc">
    <li>
        RODRIGUES, THYAGO S. ; LESAGE, DENIS ; DA SILVA, WENDER A. ; COLE, RICHARD B. ; Ebeling, G�nter ; Dupont, Ja�rton ; DE OLIVEIRA, HEIBBE C. B. ; Eberlin, Marcos N. ; NETO, BRENNO A. D. . Charge-tagged N-heterocyclic carbenes (NHC): Direct transfer from ionic liquid solutions and long-lived nature in the gas phase. <strong>JOURNAL OF THE AMERICAN SOCIETY FOR MASS SPECTROMETRY,</strong> v. 28, p. 1021-1029, 2017.
        <a href="http://dx.doi.org/10.1007/s13361-017-1637-8"><strong>Clique aqui</strong></a>
        
    </li>
</ul>
<ul type="disc">
    <li>
        MONTOLIO, SILVIA ; ABARCA, GABRIEL ; PORCAR, RA�L ; Dupont, Jairton ; BURGUETE, MAR�A ISABEL ; GARC�A-VERDUGO, EDUARDO ; LUIS, SANTIAGO V. . Hierarchically structured polymeric ionic liquids and polyvinylpyrrolidone mat-fibers fabricated by electrospinning.<strong> Journal of Materials Chemistry A,</strong> v. 5, p. 9733-9744, 2017.
        <a href="http://dx.doi.org/10.1039/C7TA02447A"><strong>Clique aqui</strong></a>
        
    </li>
</ul>
<ul type="disc">
    <li>
        LUZA, LEANDRO ; RAMBOR, CAMILA P. ; GUAL, AITOR ; ALVES FERNANDES, JESUM ; EBERHARDT, Dario ; Dupont, Jairton . Revealing Hydrogenation Reaction Pathways on Naked Gold Nanoparticles.<strong> ACS Catalysis</strong>, v. 7, p. 2791-2799, 2017.
        <a href="http://dx.doi.org/10.1021/acscatal.7b00391"><strong>Clique aqui</strong></a>
        
    </li>
</ul>
<ul type="disc">
    <li>
        LEAL, B�RBARA C. ; Aydos, Guilherme L. P. ; Netz, Paulo A. ; Dupont, Jairton . Ru-Catalyzed Estragole Isomerization under Homogeneous and Ionic Liquid Biphasic Conditions.<strong> ACS Omega</strong>, v. 2, p. 1146-1155, 2017.
        <a href="http://dx.doi.org/10.1021/acsomega.7b00078"><strong>Clique aqui</strong></a>
        
    </li>
</ul>
<ul type="disc">
    <li>
        GON�ALVES, RENATO V. ; Wender, Heberton ; MIGOWSKI, PEDRO ; Feil, Adriano F. ; EBERHARDT, Dario ; BOITA, JOCENIR ; KHAN, SHERDIL ; Machado, Giovanna ; Dupont, Jairton ; Teixeira, Sergio R. . Photochemical Hydrogen Production of Ta 2 O 5 Nanotubes Decorated with NiO Nanoparticles by Modified Sputtering Deposition. <strong>Journal of Physical Chemistry C,</strong> v. 121, p. 5855-5863, 2017.
        <a href="http://dx.doi.org/10.1021/acs.jpcc.6b10540"><strong>Clique aqui</strong></a>
        
    </li>
</ul>
<ul type="disc">
    <li>
        RAVISHANKAR, T. N. ; VAZ, MAURICIO DE O. ; RAMAKRISHNAPPA, T. ; Teixeira, Sergio R. ; DUPONT, J. . Ionic liquid assisted hydrothermal syntheses of Au doped TiO 2 NPs for efficient visible-light photocatalytic hydrogen production from water, electrochemical detection and photochemical detoxification of hexavalent chromium (Cr 6+ ).<strong> RSC Advances</strong>, v. 7, p. 43233-43244, 2017.
        <a href="http://dx.doi.org/10.1039/c7ra04944g"><strong>Clique aqui</strong></a>
        
    </li>
</ul>
<ul type="disc">
    <li>
        Dupont, Jairton; SIMON, NATHALIA M. ; ZANATTA, MARCILEIA ; DOS SANTOS, FRANCISCO P. ; CORVO, MARTA C. ; CABRITA, EURICO J. . Carbon dioxide capture by aqueous ionic liquid solutions. <strong>ChemSusChem,</strong> v. 10, p. 4927-4933, 2017.
        <a href="http://dx.doi.org/10.1002/cssc.201701044"><strong>Clique aqui</strong></a>
        
    </li>
</ul>
<ul type="disc">
    <li>
        MANJUNATH, KRISHNAPPA ; SOUZA, VIRG�NIA S. ; GANGANAGAPPA, NAGARAJU ; Scholten, Jackson D. ; TEIXEIRA, S�RGIO R. ; Dupont, Jairton ; THIPPESWAMY, RAMAKRISHNAPPA . Effect of the magnetic core of (MnFe) 2 O 3 @Ta 2 O 5 nanoparticles on photocatalytic hydrogen production.<strong> NEW JOURNAL OF CHEMISTRY,</strong> v. 41, p. 326-334, 2017.
        <a href="http://dx.doi.org/10.1039/c6nj03137d"><strong>Clique aqui</strong></a>
        
    </li>
</ul>
<ul type="disc">
    <li>
        FERNANDES, JESUM A. ; KOHLRAUSCH, EMERSON C. ; KHAN, SHERDIL ; BRITO, RAFAEL C. ; Machado, Guilherme J. ; TEIXEIRA, S�RGIO R. ; Dupont, Jairton ; LEITE SANTOS, MARCOS J. . Effect of anodisation time and thermal treatment temperature on the structural and photoelectrochemical properties of TiO 2 nanotubes. <strong>JOURNAL OF SOLID STATE CHEMISTRY,</strong> v. 251, p. 217-223, 2017.
        <a href="http://dx.doi.org/10.1016/j.jssc.2017.04.025"><strong>Clique aqui</strong></a>
        
    </li>
</ul>
<ul type="disc">
    <li>
        MANJUNATH, K. ; REDDY YADAV, L. S. ; NAGARAJU, G. ; DUPONT, J. ; RAMAKRISHNAPPA, T. . Progressive addition of GO to TiO2 nanowires for remarkable changes in photochemical hydrogen production.<strong> IONICS</strong>, v. 23, p. 2887-2894, 2017.
        <a href="http://dx.doi.org/10.1007/s11581-017-1977-1"><strong>Clique aqui</strong></a>
        
    </li>
</ul>
<ul type="disc">
    <li>
        CALABRIA, LUCIANE ; FERNANDES, JESUM ALVES ; MIGOWSKI, PEDRO ; BERNARDI, FABIANO ; BAPTISTA, DANIEL L ; Leal, Rafael ; GREHL, THOMAS ; Dupont, Jairton . Confined naked gold nanoparticles in ionic liquid films. <strong>Nanoscale,</strong> v. 9, p. 18753-18758, 2017.
        <a href="http://dx.doi.org/10.1039/c7nr06167f"><strong>Clique aqui</strong></a>
        
    </li>
</ul>
<ul type="disc">
    <li>
        NUNES, RAFAEL S. ; ALTINO, FELYPPE M. ; MENEGHETTI, MARIO R. ; MENEGHETTI, SIMONI M.P. . New mechanistic approaches for fatty acid methyl ester production reactions in the presence of Sn(IV) catalysts. <strong>CATALYSIS TODAY,</strong> v. 289, p. 121-126, 2017.
        <a href="http://dx.doi.org/10.1016/j.cattod.2016.09.016"><strong>Clique aqui</strong></a>

    </li>
</ul>
<ul type="disc">
    <li>
        DA SILVA, M�NICA ARA�JO ; DOS SANTOS, ANDERSON SELTON SILVA ; DOS SANTOS, THATIANE VER�SSIMO ; Meneghetti, Mario Roberto ; PLENTZ MENEGHETTI, SIMONI . Organotin(IV) compounds with high catalytic activities and selectivities in the glycerolysis of triacylglycerides. <strong>Catalysis Science &amp; Technology,</strong> v. 7, p. 5750-57507, 2017.
        <a href="http://dx.doi.org/10.1039/c7cy01559c"><strong>Clique aqui</strong></a>
        
    </li>
</ul>
<ul type="disc">
    <li>
        BARBOSA, ANA SORAYA LIMA ; DE SIQUEIRA GUEDES, J�SSICA ; DA SILVA, DOUGLAS ROZENDO ; MENEGHETTI, SIMONI MARGARETI PLENTZ ; Meneghetti, Mario Roberto ; DA SILVA, AMANDA EVELYN ; DE ARAUJO, MORGANA VITAL ; ALEXANDRE-MOREIRA, MAGNA SUZANA ; DE AQUINO, THIAGO MENDON�A ; DE SIQUEIRA JUNIOR, JOS� PINTO ; DE ARA�JO, RODRIGO SANTOS AQUINO ; DA CRUZ, RYLDENE MARQUES DUARTE ; MENDONÇA-JUNIOR, FRANCISCO JAIME BEZERRA . Synthesis and evaluation of the antibiotic and adjuvant antibiotic potential of organotin(IV) derivatives. <strong>JOURNAL OF INORGANIC BIOCHEMISTRY,</strong> v. 180, p. 80-88, 2017.
        <a href="http://dx.doi.org/10.1016/j.jinorgbio.2017.12.004"><strong>Clique aqui</strong></a>
    </li>
</ul>
<ul type="disc">
    <li>
        LIMA, GILVAN ; NUNES, EVERTON ; DANTAS, ROBERTA ; DE SIMONE, CARLOS ; MENEGHETTI, MARIO ; MENEGHETTI, SIMONI . Catalytic Behaviors of CoII and MnII Compounds Bearing &#945;-Diimine Ligands for Oxidative Polymerization or Drying Oils.<strong> JOURNAL OF THE BRAZILIAN CHEMICAL SOCIETY,</strong> v. 29, p. 412-418, 2017.
        <a href="http://dx.doi.org/10.21577/0103-5053.20170155"><strong>Clique aqui</strong></a>
        
    </li>
</ul>
<ul type="disc">
    <li>
        SILVA, R. S. ; OMENA, L. ; NUNES, A. M. ; DA SILVA, M. G. A. ; MENEGHETTI, M. R. ; DE OLIVEIRA, I. N. . Effects of an external electric field on the nonlinear optical absorption of smectic liquid crystals containing gold nanorods. <strong>MOLECULAR CRYSTALS AND LIQUID CRYSTALS</strong>, v. 657, p. 21-26, 2017.
        <a href="http://dx.doi.org/10.1080/15421406.2017.1402631"><strong>Clique aqui</strong></a>
        
    </li>
</ul>
<ul type="disc">
    <li>
        DA SILVA, JOS� ; DIAS, ROBERTA ; DA HORA, GABRIEL ; SOARES, THEREZA ; MENEGHETTI, MARIO . Molecular Dynamics Simulations of Cetyltrimethylammonium Bromide (CTAB) Micelles and their Interactions with a Gold Surface in Aqueous Solution. <strong>JOURNAL OF THE BRAZILIAN CHEMICAL SOCIETY</strong>, v. 29, p. 191-199, 2017.
        <a href="http://dx.doi.org/10.21577/0103-5053.20170130"><strong>Clique aqui</strong></a>
        
    </li>
</ul>
<ul type="disc">
    <li>
        D?HENI TEIXEIRA, MARIA BET�NIA ; DUARTE, MARCO ANT�NIO B. ; RAPOSO GARCEZ, LOUREINE ; CAMARGO RUBIM, JOEL ; HOFMANN GATTI, TH�R�SE ; SUAREZ, PAULO ANSELMO ZIANI . Process development for cigarette butts recycling into cellulose pulp. <strong>Waste Management (Elmsford),</strong> v. 60, p. 140-150, 2017.
        <a href="http://dx.doi.org/10.1016/j.wasman.2016.10.013"><strong>Clique aqui</strong></a>
        
    </li>
</ul>
<ul type="disc">
    <li>
        M. M. PINHO, DAVID ; A. Z. Suarez, Paulo . From Peanut Oil to Biodiesel- History and Brazilian Policyfor the Energetic Use of Fats and Oils.<strong> Revista Virtual de Qu�mica,</strong> v. 9, p. 39-51, 2017.

        <a href="http://dx.doi.org/10.21577/1984-6835.20170006"><strong>Clique aqui</strong></a>
        
    </li>
</ul>
<ul type="disc">
    <li>
        OLIVEIRA, R.S. ; MACHADO, P.M.A. ; RAMALHO, H.F. ; RANGEL, E.T. ; Suarez, P.A.Z. . Acylation of epoxidized soybean biodiesel catalyzed by SnO/Al 2 O 3 and evaluation of physical chemical and biologic activity of the product. <strong>INDUSTRIAL CROPS AND PRODUCTS</strong>, v. 104, p. 201-209, 2017.
        <a href="http://dx.doi.org/10.1016/j.indcrop.2017.04.049"><strong>Clique aqui</strong></a>
        
    </li>
</ul>
<ul type="disc">
    <li>
        MONTEIRO, ADRIANO L. ; FURLAN, MAYSA ; ZIANI SUAREZ, PAULO ANSELMO . Sistema Nacional de P�s-Gradua��so e a �rea de Qu�mica na CAPES. <strong>QUIMICA NOVA,</strong> v. 40, p. 618-625, 2017.
        <a href="http://dx.doi.org/10.21577/0100-4042.20170079"><strong>Clique aqui</strong></a>
        
    </li>
</ul>
<ul type="disc">
    <li>
        D'HENI TEIXEIRA, MARIA BET?NIA ; ALVES DE OLIVEIRA, ROBSON ; HOFMANN GATTI, TH?R?SE ; A. Z. Suarez, Paulo . The Paper: A Brief Historical Review, a Description of the Industrial Production Technology and Experiments for Preparation of Handmade Sheets.<strong> REVISTA VIRTUAL DE QU�MICA,</strong> v. 9, p. 1364-1380, 2017.
        <a href="http://dx.doi.org/10.21577/1984-6835.20170079"><strong>Clique aqui</strong></a>
        
    </li>
</ul>
<ul type="disc">
    <li>
        KOLLAR, SARA ; NOVOTNY, ETELVINO ; DO NASCIMENTO, CLAUDIA ; SUAREZ, PAULO . Nuclear Magnetic Resonance (1.40 T) and Mid Infrared (FTIR-ATR) Associated with Chemometrics as Analytical Methods for the Analysis of Methyl Ester Yield Obtained by Esterification Reaction. <strong>JOURNAL OF THE BRAZILIAN CHEMICAL SOCIETY,</strong> v. 28, p. 1917-1925, 2017.
        <a href="http://dx.doi.org/10.21577/0103-5053.20170031"><strong>Clique aqui</strong></a>
        
    </li>
</ul>
<ul type="disc">
    <li>
        MARTINS, GUILHERME ; DOS SANTOS, MARCELO ; RODRIGUES, MARCUS ; SUCUPIRA, RENATA ; MENEGHETTI, LUISA ; MONTEIRO, ADRIANO ; SUAREZ, PAULO . Cellulose Oxidation and the Use of Carboxyl Cellulose Metal Complexes in Heterogeneous Catalytic Systems to Promote Suzuki-Miyaura Coupling and C−O Bond Formation Reaction.<strong> JOURNAL OF THE BRAZILIAN CHEMICAL SOCIETY,</strong> v. 28, p. 2064-2072, 2017.
        <a href="http://dx.doi.org/10.21577/0103-5053.20170051"><strong>Clique aqui</strong></a>
        
    </li>
</ul>
<ul type="disc">
    <li>
        MARTINS, GUILHERME B. C. ; SUCUPIRA, RENATA ; Suarez, Paulo A. Z. . Papel indicador colorim�trico para detec��o de formol em produtos l�cteos e produtos de higiene pessoal.<strong> QUIMICA NOVA</strong>, v. 40, p. 946-951, 2017.
        <a href="http://dx.doi.org/10.21577/0100-4042.20170102"><strong>Clique aqui</strong></a>
        
    </li>
</ul>
<ul type="disc">
    <li>
        PINHO, DAVID ; OLIVEIRA, RENATO ; DOS SANTOS, VITOR ; MARQUES, WELINGTON ; PINTO, ANGELO ; REZENDE, MICHELLE ; SUAREZ, PAULO . Evaluating the Potential of Biodiesel Production through Microalgae Farming in Photobioreactor and High Rate Ponds from Wastewater Treatment.<strong> JOURNAL OF THE BRAZILIAN CHEMICAL SOCIETY</strong>, v. 28, p. 2429-2437, 2017.
        <a href="http://dx.doi.org/10.21577/0103-5053.20170097"><strong>Clique aqui</strong></a>
        
    </li>
</ul>
<ul type="disc">
    <li>
        ADORNO, RODRIGO R. ; DO CARMO, DERMEVAL A. ; GERMS, GERARD ; WALDE, DETLEF H.G. ; DENEZINE, MATHEUS ; BOGGIANI, PAULO C. ; SOUSA E SILVA, SIMONE C. ; VASCONCELOS, JULIANA R. ; TOBIAS, THA�S C. ; GUIMAR�ES, EDI M. ; VIEIRA, LUCIETH C. ; FIGUEIREDO, MILENE F. ; MORAES, RENATO ; CAMINHA, SILANE A. ; Suarez, Paulo A.Z. ; RODRIGUES, CHRISTIAN V. ; CAIXETA, GUILHERME M. ; PINHO, DAVID ; SCHNEIDER, GABI ; MUYAMBA, RALPH . Cloudina lucianoi ( Beurlen and Sommer, 1957 ), Tamengo Formation, Ediacaran, Brazil: Taxonomy, Analysis of Stratigraphic Distribution and Biostratigraphy. <strong>PRECAMBRIAN RESEARCH,</strong> v. 301, p. 19-35, 2017.
        <a href="http://dx.doi.org/10.1016/j.precamres.2017.08.023"><strong>Clique aqui</strong></a>
        
    </li>
</ul>
<ul type="disc">
    <li>
        P�RES, EDUARDO ULISSES XAVIER ; SOUSA, MARCELO HENRIQUE ; GOMES DE SOUZA, FERNANDO ; Machado, Fabricio ; SUAREZ, PAULO ANSELMO ZIANI . Synthesis and characterization of a new biobased poly(urethane-ester) from ricinoleic acid and its use as biopolymeric matrix for magnetic nanocomposites. <strong>EUROPEAN JOURNAL OF LIPID SCIENCE AND TECHNOLOGY</strong>, v. 119, p. 1600451-1600462, 2017.
        <a href="http://dx.doi.org/10.1002/ejlt.201600451"><strong>Clique aqui</strong></a>
        
    </li>
</ul>
<ul type="disc">
    <li>
        BRAGA, LILIAN RODRIGUES ; RANGEL, ELLEN TANUS ; SUAREZ, PAULO ANSELMO ZIANI ; Machado, Fabricio . Simple synthesis of active films based on PVC incorporated with silver nanoparticles: Evaluation of the thermal, structural and antimicrobial properties.<strong> FOOD PACKAGING AND SHELF LIFE,</strong> v. 15, p. 122-129, 2017.
        <a href="http://dx.doi.org/10.1016/j.fpsl.2017.12.005"><strong>Clique aqui</strong></a>
    </li>
</ul>
<ul type="disc">
    <li>
        ALMERINDO, GIZELLE ; GABORIM, ANIKA ; NICOLAZI, LUCAS ; Idrees, Muhammad ; Nome, Faruk ; FIEDLER, HAIDI ; NOME, RENE . Confocal Fluorescence Microscopy and Kinetics of the Cr3+-Chromate Ion Oxidation Equilibria at the Solid Liquid Interface. <strong>JOURNAL OF THE BRAZILIAN CHEMICAL SOCIETY,</strong> v. -, p. 1708-1714, 2017.
        <a href="http://dx.doi.org/10.21577/0103-5053.20170015"><strong>Clique aqui</strong></a>

    </li>
</ul>
<ul type="disc">
    <li>
        NOME, RENE A; SORBELLO, CECILIA ; JOBB�GY, MAT�AS ; BARJA, BEATRIZ C ; SANCHES, VITOR ; CRUZ, JOYCE S ; AGUIAR, VINICIUS F . Rich stochastic dynamics of co-doped Er:Yb fluorescence upconversion nanoparticles in the presence of thermal, non-conservative, harmonic and optical forces.<strong> Methods and Applications in Fluorescence,</strong> v. 5, p. 014005, 2017.
        <a href="http://dx.doi.org/10.1088/2050-6120/aa5a81"><strong>Clique aqui</strong></a>
        
    </li>
</ul>
<ul type="disc">
    <li>
        NOME, REN� A.; COSTA, AMANDA F. ; LEPKOSKI, JESSICA ; MONTEIRO, GABRIEL A. ; HAYASHI, JULIANO G. ; CORDEIRO, CRISTIANO M. B. . Characterizing Slow Photochemical Reaction Kinetics by Enhanced Sampling of Rare Events with Capillary Optical Fibers and Kramers? Theory.<strong> ACS Omega,</strong> v. 2, p. 2719-2727, 2017.
        <a href="http://dx.doi.org/10.1021/acsomega.7b00004"><strong>Clique aqui</strong></a>
        
    </li>
</ul>
<ul type="disc">
    <li>
        GEROLA, ADRIANA P. ; WANDERLIND, EDUARDO H. ; GOMES, YASMIN S. ; GIUSTI, LUCIANO A. ; GARC�A-R�O, LUIS ; NOME, REN� A. ; KIRBY, ANTHONY J. ; Fiedler, Haidi D. ; Nome, Faruk . Supramolecular Polymer/Surfactant Complexes as Catalysts for Phosphate Transfer Reactions. <strong>ACS Catalysis</strong>, v. 7, p. 2230-2239, 2017.
        <a href="http://dx.doi.org/10.1021/acscatal.7b00097"><strong>Clique aqui</strong></a>
    </li>
</ul>
<ul type="disc">
    <li>
        BALESTRIN, LIA BERALDO DA SILVEIRA ; CARDOSO, MATEUS BORBA ; Loh, Watson . Using atomic force microscopy to detect asphaltene colloidal particles in crude oils. <strong>Energy &amp; Fuels (Print)</strong>, v. x, p. acs.energyfuels.6b03333, 2017.
        <a href="http://dx.doi.org/10.1021/acs.energyfuels.6b03333"><strong>Clique aqui</strong></a>
    </li>
</ul>
<ul type="disc">
    <li>
        PARINAZ AKHLAGHI, SEYEDEH ; Loh, Watson . Interactions and Release of Two Palmitoyl Peptides from Phytantriol Cubosomes. <strong>European Journal of Pharmaceutics and Biopharmaceutics</strong>, v. xx, p. y, 2017.
        <a href="http://dx.doi.org/10.1016/j.ejpb.2017.03.022"><strong>Clique aqui</strong></a>
        
    </li>
</ul>
<ul type="disc">
    <li>
        DOS SANTOS, RONALDO GON�ALVES ; BRINCE�O, MARIA ISABEL ; Loh, Watson . Laminar pipeline flow of heavy oil-in-water emulsions produced by continuous in-line emulsification.<strong>JOURNAL OF PETROLEUM SCIENCE AND ENGINEERING</strong>, v. x, p. y, 2017.
        <a href="http://dx.doi.org/10.1016/j.petrol.2017.06.061"><strong>Clique aqui</strong></a>
        
    </li>
</ul>
<ul type="disc">
    <li>
        Loh, Watson; SILVEIRA, N�DYA PESCE DA . A mat�ria mole e a luz s�ncrotron. CI�NCIA E CULTURA, v. 69, p. 47-51, 2017.
        <a href="http://dx.doi.org/10.21800/2317-66602017000300014"><strong>Clique aqui</strong></a>
        
    </li>
</ul>
<ul type="disc">
    <li>
        FERREIRA, GUILHERME A. ; Loh, Watson . Liquid crystalline nanoparticles formed by oppositely charged surfactant-polyelectrolyte complexes. <strong>CURRENT OPINION IN COLLOID &amp; INTERFACE SCIENCE,</strong> v. x, p. y, 2017.
        <a href="http://dx.doi.org/10.1016/j.cocis.2017.08.003"><strong>Clique aqui</strong></a>
        
    </li>
</ul>
<ul type="disc">
    <li>
        CARNEIRO, NATHALIA M. ; PERCEBOM, ANA M. ; Loh, Watson . Quest for Thermoresponsive Block Copolymer Nanoparticles with Liquid-Crystalline Surfactant Cores. <strong>ACS Omega,</strong> v. 2, p. 5518-5528, 2017.
        <a href="http://dx.doi.org/10.1021/acsomega.7b00905%3Cstrong%3E"><strong>Clique aqui</strong></a>	
    </li>
</ul>
<ul type="disc">
    <li>
        OLIVEIRA, VANESSA A. ; IGLESIAS, BERNARDO A. ; AURAS, BRUNA L. ; Neves, Ademir ; TERENZI, Hern�n . Photoactive meso-tetra(4-pyridyl)porphyrin-tetrakis-[chloro(2,2-bipyridine)platinum( ii ) derivatives recognize and cleave DNA upon irradiation. <strong>Dalton Transactions (2003. Print)</strong>, v. 46, p. 1660-1669, 2017.
        <a href="http://dx.doi.org/10.1039/c6dt04634g"><strong>Clique aqui</strong></a>

    </li>
</ul>
<ul type="disc">
    <li>
        PIVETTA, RHANNANDA C. ; AURAS, BRUNA L. ; Souza, Bernardo de ; Neves, Ademir ; NUNES, F�BIO S. ; COCCA, LEANDRO H.Z. ; BONI, LEONARDO DE ; IGLESIAS, BERNARDO A. . Synthesis, photophysical properties and spectroelectrochemical characterization of 10-(4-methyl-bipyridyl)-5,15-(pentafluorophenyl)corrole. Journal of Photochemistry and Photobiology<strong> A: Chemistry,</strong> v. 332, p. 306-315, 2017.
        <a href="http://dx.doi.org/10.1016/j.jphotochem.2016.09.008"><strong>Clique aqui</strong></a>
        
    </li>
</ul>
<ul type="disc">
    <li>
        SILVA, GRACIELA APARECIDA DOS SANTOS ; AMORIM, ANDR� ; Souza, Bernardo de ; GABRIEL, PHILIPE ; TERENZI, HERNAN ; NORDLANDER, EBBE ; Neves, Ademir ; PERALTA, ROSELY . Synthesis and characterization of FeIII(&#956;-OH)ZnII complexes: Effects of second coordination sphere and increase in the chelate ring size on the hydrolysis of a phosphate diester and DNA.<strong> DALTON TRANSACTIONS,</strong> v. 46, p. 11380-11394, 2017.
        <a href="http://dx.doi.org/10.1039/c7dt02035j"><strong>Clique aqui</strong></a>
        
    </li>
</ul>
<ul type="disc">
    <li>
        CAMARGO, TIAGO PACHECO ; Neves, Ademir ; PERALTA, Rosely A. ; CHAVES, CL�UDIA ; MAIA, ELENE C. P. ; LIZARAZO-JAIMES, EDGAR H. ; GOMES, DAWIDSON A. ; Bortolotto, Tiago ; NORBERTO, DOUGLAS R. ; TERENZI, Hern�n ; TIERNEY, DAVID L. ; SCHENK, Gerhard . Second-Sphere Effects in Dinuclear Fe III Zn II Hydrolase Biomimetics: Tuning Binding and Reactivity Properties. <strong>INORGANIC CHEMISTRY,</strong> v. 57, p. 187-203, 2017.
        <a href="http://dx.doi.org/10.1021/acs.inorgchem.7b02384"><strong>Clique aqui</strong></a>
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
        pesq_list[cont] = pesq_list[cont].split(', ')
        pesq_list[cont] = (pesq_list[cont][1] + ' ' + pesq_list[cont][0]).title().strip()
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
    artigo["publicador"] = info[0].title()
    artigo["versao"] = info[1][3:]
    artigo["paginas"] = info[2][3:]
    artigo["ano"] = int(info[3])
    artigo["link"] = link

    for key in artigo:
        print(key, "=", artigo[key])

    #inp = input("Ok?")
    #entrei = 0
    #if(inp != ''):
    #    entrei = 1
    #    break

    json_file.append(artigo)

#if not entrei:
with open('jsonForScript.json', 'w') as file:
    json.dump(json_file, file)