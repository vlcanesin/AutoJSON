from bs4 import BeautifulSoup
import json

html = """
    <ul type="disc">
        <li>1)	 ALBERTO, E. E.; NASCIMENTO, V.; BRAGA, A. L. . Catalytic Application of Selenium and Tellurium Compounds as Glutathione Peroxidase Enzyme Mimetics.<strong>Journal of the Brazilian Chemical Society</strong>, v. 21, pp 2032 - 2041, 2010.</li>
    </ul>
    <ul type="disc">
        <li>2)	 ALLIPRANDINI-FILHO, P.; BORGES, G.F.; CALIXTO, W.B.; BECHTOLD, I.H.; VIEIRA, A.A.; CRISTIANO, R.; GALLARDO, H.; SILVA, R.A.; NETO, N.M. BARBOSA, M.A. . Molecular alignment effects on spectroscopic properties 2,1,3-benzothiadiazole guested in liquid crystalline compounds. <strong>Chemical Physics Letters</strong>, v. 487, pp 263-267, 2010.</li>
    </ul>
    <ul type="disc">
        <li>3)	 ALMEIDA, C. A. P.; SANTOS, A.; JAERGER, S.; DEBACHER, N. A.; HANKINS, N. . Mineral waste from coal mining for removal of astrazon red dye from aqueous solutions. <strong>Desalination (Amsterdam)</strong>, v. 264, pp 181 - 187, 2010.</li>
    </ul>
    <ul type="disc">
        <li>4)	 ALVAREZ, G.; GERPE, A.; BENITEZ, D.; GARIBOTTO, F.; ZACCHINO, S.; GRAEBIN, C. S.; DA ROSA, R. G.; EIFLER-LIMA, V. L.; GONZALEZ, M.; CERECETTO, H. . New Limonene-Hybrid Derivatives with Anti-T. cruzi Activity. <strong>Letters in Drug Design &amp; Discovery</strong>, v. 7, pp 452-60, 2010.</li>
    </ul>
    <ul type="disc">
        <li>5)	 ALVES, M. B.; MEDEIROS, F. C. M.; SUAREZ, P. A. Z. . Cadmium compounds as Catalysts for Biodiesel.  <strong>Industrial & engineering chemistry research</strong>, v. 49, p. 7176-7182, 2010.</li>
    </ul>
    <ul type="disc">
        <li>6)	 ALVES, M. B.; UMPIERRE, A. P.; SANTOS, V. O.; SOARES, V. C. D.; DUPONT, J.; RUBIM, J. C.; SUAREZ, P. A. Z. . The use of Differential Scanning Calorimetry (DSC) to characterize phase diagrams of ionic mixtures of 1-n-butyl-3-methylimidazolium chloride and niobium chloride or zinc chloride. <strong>Thermochimica Acta</strong>, v. 502, pp 20-3, 2010.</li>
    </ul>
    <ul type="disc">
        <li>7)	 ARELARO, A. D.; ROSSI, L. M.; RECHENBERG, H. R. . In-field M�ssbauer characterization of MFe O (M = Fe, Co, Ni) nanoparticles. <strong>Journal of Physics: Conference Series (Online)</strong>, v. 217, pp 012126, 2010.</li>
    </ul>
    <ul type="disc">
        <li>8)	 BARBETA, V. B.; JARDIM, R. F.; KIYOHARA, P. K.; EFFENBERGER, F. B.; ROSSI, L. M. . Magnetic properties of Fe3O4 nanoparticles coated with oleic and dodecanoic acids. <strong>Journal of Applied Physics</strong>, v. 107, pp 73913, 2010.</li>
    </ul>
    <ul type="disc">
        <li>    BERLAMINO, A. T. N.; ORTH, E.S.; MELLO, R.S.; al., et . Catalytic nanoreactors for ester hydrolysis. <strong>Journal of Molecular Catalysis A-Chemical</strong>, v. 332, pp 7-12, 2010.</li>
    </ul>
    <ul type="disc">
        <li>10)	 BERNARDES, J. S.; SILVA, M. A.; PICULELL, L.; LOH, W. . Reverse micelles with spines: L2 phases f surfactant ion-polyion complex salts, n-alcohols and water investigated by rheology, NMR diffusion and SAXS measurements. <strong>Soft Matter</strong>, v. 6, pp 144-153, 2010.</li>
    </ul>
    <ul type="disc">
        <li>11)	BITENCOURT, T. B.; NASCIMENTO, M. G. . The Influence Of Organic Solvent And Ionic Liquids On The Selective Formation Of 2-(2-Ethylhexyl)-3-Phenyl-1,2-Oxaziridine Mediated By Lipases. <strong>Journal of Physical Organic Chemistry</strong>, v. 23, pp 995-999, 2010.</li>
    </ul>
    <ul type="disc">
        <li>12)	BORTOLUZZI, A. J.; SOUZA, L. B. P.; JOUSSEF, A. C. . (3R,8aS)-3-Ethylperhydropyrrolo[1,2-a]pyrazine-1,4-dione. <strong>Acta Crystallographica Section E-Structure Reports Online</strong>, v. 66, pp O417-U2999, 2010.</li>
    </ul>
    <ul type="disc">
        <li>13)	BRAGA, A.; WESSJOHANN, L.; TAUBE, P.; GALETTO, F.; ANDRADE, F. DE. . Straightforward Method for the Synthesis of Selenocysteine and Selenocystine Derivatives from l-Serine Methyl Ester. <strong>Synthesis (Stuttgart)</strong>, v. -, pp 3131 - 3137, 2010.</li>
    </ul>
    <ul type="disc">
        <li>14)	BRAGA, H. C.; STEFANI, H. A.; PAIX�O, M. W.; SANTOS, F. W.; LUDTKE, D. S. . Synthesis of 5 '-seleno-xylofuranosides. <strong>Tetrahedron</strong>, v. 66, pp 3441-3446, 2010.</li>
    </ul>
    <ul type="disc">
        <li>15)	BRONDANI, D.; VIEIRA, I. C.; PIOVEZAN, C.; DA SILVA, J. M. R.; NEVES, A.; DUPONT, J.; SCHEEREN, C. W. . Sensor for fisetin based on gold nanoparticles in ionic liquid and binuclear nickel complex immobilized in silica. <strong>Analyst</strong>, v. 135, pp 1015-22, 2010.</li>
    </ul>
    <ul type="disc">
        <li>16)	CAMARGO, M. A.; NEVES, A.; BORTOLUZZI, A. J.; SZPOGANICZ, B.; FISCHER, F. L.; TERENZI, H.; SERRA, O. A.; SANTOS, V. G.; VAZ, B. G.; EBERLIN, M. N. . Efficient Phosphodiester Hydrolysis by Luminescent Terbium(III) and Europium(III) Complexes. <strong>Inorganic Chemistry</strong>, v. 49, pp 6013-6025, 2010.</li>
    </ul>
    <ul type="disc">
        <li>17)	CAMARGO, M. A.; NEVES, A.; SZPOGANICZ, B.; BORTOLUZZI, A. J.; FISCHER, F. L.; TERENZI, H.; CASTELLANO, E. E. . Synthesis, Structure, and Phosphatase-Like Activity of a New Trinuclear Gd Complex with the Unsymmetrical Ligand H3L As a Model for Nucleases. <strong>Inorganic Chemistry</strong>, v. 49, pp 3057-3063, 2010.</li>
    </ul>
    <ul type="disc">
        <li>18)	CARROLL, F. A.; LIN, C. Y.; QUINA, F. H. . Improved Prediction of Hydrocarbon Flash Points from Boiling Point Data. <strong>Energy &amp; Fuels</strong>, v. 24, pp 4854-4856, 2010.</li>
    </ul>
    <ul type="disc">
        <li>19)	CASARANO, R.; FIDALE, L. C.; LUCHETI, C. M.; HEINZE, T.; EL SEOUD, O. A. . Expedient, accurate methods for the determination of the degree of substitution of cellulose carboxylic esters: Application of Uv-vis spectroscopy (dye solvatochromism) and FTIR. <strong>Carbohydrate Polymers</strong>, v. 83, pp1285-1292, 2010.</li>
    </ul>
    <ul type="disc">
        <li>20)	CASTAGNO, K. R. L.; DALMORO, V.; MAULER, R. S.; AZAMBUJA, D. S. . Characterization and corrosion protection properties of polypyrrole/montmorillonite electropolymerized onto aluminium alloy 1100. <strong>Journal of Polymer Research</strong>, v. 17, pp 647-55, 2010. </li>
    </ul>
    <ul type="disc">
        <li>21)	CIACCO, G. T.; MORGADO, D. L.; FROLLINI, E.; POSSIDONIO, S.; EL SEOUD, O. A. . Some aspects of acetylation of untreated and mercerized sisal cellulose. <strong>Journal of Brazilian Chemical Society</strong>, v. 21, pp 71-77, 2010.</li>
    </ul>
    <ul type="disc">
        <li>22)	COELHO, S. E.; TERRA, G. G.; BORTOLUZZI, A. J. . Di-mu-chlorido-bis{[2-({[2-(2-pyridyl)-ethyl](2-pyridylmethyl)amino}methyl)phenol]zinc(II)} bis(perchlorate) dehydrate. <strong>Acta Crystallographica Section E-Structure Reports Online</strong>, v. 66, pp M229-U1349, 2010.</li>
    </ul>
    <ul type="disc">
        <li>23)	CONSORTI, C. S.; AYDOS, G. L. P.; DUPONT, J. . Tandem isomerisation-metathesis catalytic processes of linear olefins in ionic liquid biphasic system. <strong>Chemical Communications</strong>, v. 46, pp 9058-60,  2010.</li>
    </ul>
    <ul type="disc">
        <li>24)	CONTESINI, F. J.; LOPES, D. B.; MACEDO, G. A.; CARVALHO, P. O.; NASCIMENTO, M. G. . Aspergillus Sp Lipase: Potential Biocatalyst For Industrial Use. <strong>Journal of Molecular Catalysis B: Enzymatic</strong>, v. 67, pp 163-171, 2010.</li>
    </ul>
    <ul type="disc">
        <li>25)	COSTA, L. A. F.; BREYER, H. S.; RUBIM, J. C. . Surface-enhanced Raman scattering (SERS) on copper electrodes in 1-n-butyl-3-methylimidazoliun tetrafluorbarate (BMI.BF4): The adsorption of benzotriazole (BTAH). <strong>Vibrational Spectroscopy</strong>, v. 54, pp 103-106, 2010.   </li>
    </ul>
    <ul type="disc">
        <li>26)	COSTA, J. C. S.; CORDEIRO, D. S.; SANT ANA, A. C.; ROSSI, L. M.; SANTOS, P. S.; CORIO, P. . Sensing of 2,4-dichlorophenoxyacetic acid by surface-enhanced Raman scattering. <strong>Vibrational Spectroscopy</strong>, v. 54, pp 133-136, 2010. </li>
    </ul>
    <ul type="disc">
        <li>27)	COSTA, N. J. S.; KIYOHARA, P. K.; MONTEIRO, A. L.; COPPEL, Y.; PHILIPPOT, K.; ROSSI, L. M. . A single-step procedure for the preparation of palladium nanoparticles and a phosphine-functionalized support as catalyst for Suzuki cross-coupling reactions. <strong>Journal of Catalysis</strong>, v. 276, pp 382-389, 2010.</li>
    </ul>
    <ul type="disc">
        <li>28)	COSTA, V. V.; ROCHA, K. A. DA S.; KOZHEVNIKOV, I. V.; GUSEVSKAYA, E. V. . Isomerization of styrene oxide to phenylacetaldehyde over supported phosphotungstic heteropoly acid. <strong>Applied Catalysis</strong>- A, v. 383, p. 215-220, 2010.</li>
    </ul>
    <ul type="disc">
        <li>29)	DAL CASTEL, C.; PELEGRINI, T.; BARBOSA, R. V.; LIBERMAN, S. A.; MAULER, R. S. . Properties of silane grafted polypropylene/montmorillonite nanocomposites. <strong>Composites Part A-Applied Science And Manufacturing</strong>, v. 41, pp 185-191, 2010.  </li>
    </ul>
    <ul type="disc">
        <li>30)	DARENSBOURG, D. J.; HORN JR, A.; MONCADA, A. I.  . A facile catalytic synthesis of trimethylene carbonate from trimethylene oxide and carbon dioxide. <strong>Green Chemistry</strong>, v. 12, pp 1376-1379, 2010.</li>
    </ul>
    <ul type="disc">
        <li>31)	DEOBALD, A. M.; SIMON DE CAMARGO, L. R.; TABARELLI, G.; H�RNER, M.; RODRIGUES, O. E.D.; ALVES, D.; BRAGA, A. L. . Synthesis of azido arylselenides and azido aryldiselenides: a new class of selenium/nitrogen compounds. <strong>Tetrahedron Letters</strong>, v 51, pp 3364 - 3367, 2010.</li>
    </ul>
    <ul type="disc">
        <li>32)	DIAS, R.P.; MAURO, S. L. P. J.; ALMEIDA, W. B. DE; ROCHA, W. R. . DFT Study of The Ligands Effects on the Regioselectivity of the Insertion Reaction of Olefins in the Complexes [HRh(CO)2(PR3)(L)] (R=H,F,Et,Ph,OEt,OPh and L=Propene, Styrene). <strong>International Journal of Quantum Chemistry</strong>, v. 111, pp 1280-1292, 2010.  </li>
    </ul>
    <ul type="disc">
        <li>33)	DONATO, R. K.; BENVEGNU, M. A.; FURLAN, L. G.; MAULER, R. S.; SCHREKKER, H. S. . Imidazolium Salts as Liquid Coupling Agents for the Preparation of Polypropylene-Silica Composites. <strong>Journal of Applied Polymer Science</strong>, v. 116, pp 304-307, 2010.  </li>
    </ul>
    <ul type="disc">
        <li>34)	DUPONT, J.; SCHOLTEN, J. D. . On the structural and surface properties of transition-metal nanoparticles in ionic liquids. <strong>Chemical Society Reviews</strong>, v. 39, pp 1780-804, 2010.</li>
    </ul>
    <ul type="disc">
        <li>35)	ECCHER, J.; SAMPAIO, A. R.; VISCOVINI, R. C.; CONTE, G.; WESPHAL, E.; GALLARDO, H.; BECHTOLD, I. H. . Image processing as a tool for phase transitions identification. <strong>Journal of Molecular Liquid</strong>, v. 153, pp 162-166, 2010.  </li>
    </ul>
    <ul type="disc">
        <li>36)	EL SEOUD, O. A.; RAMADAN, A. D.; SATO, B. M. . Surface properties of calcinated titanium dioxide probed by solvatochromic indicators: Relevance to catalytic applications. <strong>Journal of Physical Chemistry C</strong>, v. 114, pp 10436-10443, 2010.</li>
    </ul>
    <ul type="disc">
        <li>37)	EL SEOUD, OMAR A. . Solvation simplified. <strong>Qu�mica Nova</strong>, v. 33, pp 2187-2192, 2010.</li>
    </ul>
    <ul type="disc">
        <li>38)	FAJARDO, H. V.; LONGO, E.; MEZALIRA, D. Z.; NUERNBERG, G. B.; ALMERINDO, G. I.; COLLASIOL, A.; PROBST, L. F. D.; GARCIA, I. T. S.; CARRENO, N. L. V. . Influence of support on catalytic behavior of nickel catalysts in the steam reforming of ethanol for hydrogen production. <strong>Environmental Chemistry Letters</strong>, v. 8, pp 79-85, 2010. </li>
    </ul>
    <ul type="disc">
        <li>39)	FARIA, R. B.; NEVES, A. . Uso de Equa��es Lineares na Determina��o dos Par�metros de Michaelis-Menten. <strong>Qu�mica Nova</strong>, v. 33, pp 1607-1611, 2010.</li>
    </ul>
    <ul type="disc">
        <li>40)	FEIL, A. F.; COSTA, M. V.; AMARAL, L.; TEIXEIRA, S. R.; MIGOWSKI, P.; DUPONT, J.; MACHADO, G.; PERIPOLLI, S. B. . The influence of aluminum grain size on alumina nanoporous structure. <strong>Journal of Applied Physics</strong>, v. 107, pp 026103, 2010.  </li>
    </ul>
    <ul type="disc">
        <li>41)	FEIL, A. F.; MIGOWSKI, P.; SCHEFFER, F. R.; PIEROZAN, M. D.; CORSETTI, R. R.; RODRIGUES, M.; PEZZI, R. P.; MACHADO, G.; AMARAL, L.; TEIXEIRA, S. R.; al, et . Growth of TiO2 Nanotube Arrays with Simultaneous Au Nanoparticles Impregnation: Photocatalysts for Hydrogen Production. <strong>Journal of the Brazilian Chemical Society</strong>, v. 21, pp 1359-1365, 2010.</li>
    </ul>
    <ul type="disc">
        <li>42)	FERNANDES, A. N.; ALMEIDA, C. A. P.; DEBACHER, N. A.; SIERRA, M. M. DE S. . Isotherm and thermodynamic data of adsorption of methylene blue from aqueous solution onto peat. <strong>Journal of Molecular Structure</strong>, v. 982, pp 62 - 65, 2010.</li>
    </ul>
    <ul type="disc">
        <li>43)	FERNANDES, C. ; HORN JR., A.; VIEIRA-DA-MOTTA, O.; ASSIS, V.M.; ROCHA, M. R. ; MATHIAS, L. DA S.; BULL, E. S.; BORTOLUZZI, A. J.; GUIMAR�ES, E. V.; ALMEIDA, J. C. A.; RUSSELL, D. H. . Synthesis, characterization and antibacterial activity of FeIII, CoII, CuII and ZnII complexes probed by transmission electron microscopy. <strong>Journal of Inorganic Biochemistry</strong>, v. -, pp 1214 - 1223, 2010.</li>
    </ul>
    <ul type="disc">
        <li>44)	FERNANDES, C.; MOREIRA, R. O.; LUBE, L. M.; HORN JR, A.; SZPOGANICZ, B.; SHERROD, S.; RUSSELL, D. H. . Investigation of the interaction of iron(iii) complexes with dAMP by ESI-MS, MALDI-MS and potentiometric titration: insights into synthetic nuclease behavior. <strong>Dalton Transactions</strong>, v. 39, pp 5094 - 5100, 2010.</li>
    </ul>
    <ul type="disc">
        <li>45)	FERNANDES, S. C.; VIEIRA, I. C.; PERALTA, R. A.; NEVES, A. . Development of a biomimetic chitosan film-coated gold electrode for determination of dopamine in the presence of ascorbic acid and uric acid. <strong>Electrochimica Acta</strong>, v. 55, pp 7152-7157, 2010.</li>
    </ul>
    <ul type="disc">
        <li>46)	FERREIRA, D. E. C.; DE ALMEIDA, W. B.; NEVES, A.; ROCHA, W. R. . Broken Symmetry Density Functional Study of a Mixed-valence Unsymmetrical Dinuclear Iron Complex. <strong>International Journal Of Quantum Chemistry</strong>, v. 110, pp 1048-1055, 2010.  </li>
    </ul>
    <ul type="disc">
        <li>47)	FERREIRA, T. L.; SATO, B. M.; EL SEOUD, O. A.; BERTOTTI, M. . Application of Microelectrode Voltammetry to Study the Properties of Surfactant Solutions: Alkyltrimethylammonium Bromides. <strong>Journal of Physical Chemistry B</strong>, v. 114, pp 857-862, 2010.  </li>
    </ul>
    <ul type="disc">
        <li>48)	FIDALE, L. C.; BR�CKER, C.; SILVA, P. L.; LUCHETI, C. M.; HEINZE, T.; EL SEOUD, O. A. . Probing the dependence of the properties of cellulose acetates and their films on the degree of biopolymer substitution: Use of solvatochromic indicators and thermal analysis. <strong>Cellulose</strong>, v. 17, pp 937-951, 2010.</li>
    </ul>
    <ul type="disc">
        <li>49)	FRANZOI, A. C.; VIEIRA, I. C.; DUPONT, J. . Biosensors of Laccase Based on Hydrophobic Ionic Liquids Derived from Imidazolium Cation. <strong>Journal of the Brazilian Chemical Society</strong>, v. 21, pp 1451-8, 2010.</li>
    </ul>
    <ul type="disc">
        <li>50)	FRANZOI, A. C.; VIEIRA, I. C.; SCHEEREN, C. W.; DUPONT, J. . Development of Quercetin Biosensor Through Immobilizing Laccase in a Modified beta-Cyclodextrin Matrix Containing Ag Nanoparticles in Ionic Liquid. <strong>Electroanalysis</strong>, v. 22, pp 1376-85, 2010.</li>
    </ul>
    <ul type="disc">
        <li>51)	FREDERICE, R.; FERREIRA, A. P. G.; GEHLEN, M. H. . Molecular Fluorescence in Silica Particles Doped with Quercetin-Al3+ Complexes. <strong>Journal of Brazilian Chemical Society</strong>, v. 21, pp 1213 - 1217, 2010.</li>
    </ul>
    <ul type="disc">
        <li>52)	FREITAS, A. A.; QUINA, F. H.; FERNANDES, A. C.; MA�ANITA, A. . Picosecond Dynamics of the Prototropic Reactions of 7-Hydroxyflavylium Photoacids Anchored at an Anionic Micellar Surface. <strong>Journal of Physical Chemistry A</strong>, v. 114, pp 4188-4196, 2010.</li>
    </ul>
    <ul type="disc">
        <li>53)	GALGANO, P. D.; EL SEOUD, O. A. . Surface active ionic liquids: Comparison of the micellar properties of 1-hexadecyl-3-methylimidazolium chloride with other cationic surfactants. <strong>Journal of Colloid and Interface Science</strong>, v. 345, pp 1-11, 2010.</li>
    </ul>
    <ul type="disc">
        <li>54)	GALLARDO, H.; GIROTTO, E.; BORTOLUZZI, A.J. . 1-(5-Hydroxy-1-phenyl-3-trifluoromethyl-1-pyrazol-1-yl)ethanone. <strong>Acta Crystallographica</strong> - Section E, v. 66, pp 75-76, 2010.  </li>
    </ul>
    <ul type="disc">
        <li>55)	GALLARDO, H.; SANTOS, D. M. P. O.; BORTOLUZZI, A. J. . 2-(4-Bromophenyl)-5-dodecyloxy-1,3-thiazole.<strong>Acta Crystallographica</strong> - Section E, v. 66, pp 2365-2365, 2010.</li>
    </ul>
    <ul type="disc">
        <li>56)	GAY, R. M.; MANARIN, F.; BRAND�O, R.; ZENI, G. . Palladium Catalyzed Suzuki Cross-Coupling of 3-Iodo-2-(methylthio)-benzo[b]furan Derivatives: Synthesis of 3-Aryl-2-(methylthio)benzo[b]furans. <strong>Journal of the Brazilian Chemical Society</strong>, v. 21, pp 1635-1641, 2010.</li>
    </ul>
    <ul type="disc">
        <li>57)	GAY, R. M.; MANARIN, F.; SCHNEIDER, C. C.; BARANCELLI, D. A.; COSTA, M. D.; ZENI, G. . FeCl -Diorganyl Dichalcogenides Promoted Cyclization of 2-Alkynylanisoles to 3-Chalcogen Benzo[ ]furans. <strong>Journal of Organic Chemistry</strong>, v. 75, pp 5701-5706, 2010.</li>
    </ul>
    <ul type="disc">
        <li>58)	GEHLEN, M. H. . Kinetics of autocatalytic acid hydrolysis of cellulose with crystalline and amorphous fractions. <strong>Cellulose</strong>, v. 17, pp 245-252, 2010.  </li>
    </ul>
    <ul type="disc">
        <li>59)	GERICKE, M.; LIEBERT, T.; EL SEOUD, O. A.; HEINZE, T. . Tailored Media for Homogeneous Cellulose Chemistry: Ionic Liquid/Co-Solvent Mixtures.  <strong>Macromolecular Materials and Engineering</strong>, v. 296, pp 483-493, 2010.</li>
    </ul>
    <ul type="disc">
        <li>60)	GIUSTI, LUCIANO A.; MACHADO, V. G. . A non-enzymatic model based on an acyl transfer reaction for the formation of energy-rich acetyl phosphate in organic solvents and in a biphasic system. <strong>Journal of Physical Organic Chemistry</strong>, v. 23, pp 735-742, 2010.</li>
    </ul>
    <ul type="disc">
        <li>61)	GODINHO, M.; GONCALVES, R. D.; LEITE, E. R.; RAUBACH, C. W.; CARRENO, N. L. V.; PROBST, L. F. D.; LONGO, E.; FAJARDO, H. V. . Gadolinium-doped cerium oxide nanorods: novel active catalysts for ethanol reforming. <strong>Journal of Materials Science</strong>, v. 45, pp 593-598, 2010. </li>
    </ul>
    <ul type="disc">
        <li>62)	GODOI, M.; ALBERTO, E. E.; PAIX�O, M. W.; SOARES, L. A.; SCHNEIDER, P. H.; BRAGA, A. L. . New class of amino-phosphinite chiral catalysts for the highly enantioselective addition of arylzinc reagents to aldehydes. <strong>Tetrahedron</strong>, v. 66, pp 1341 - 1345, 2010.  </li>
    </ul>
    <ul type="disc">
        <li>63)	GRAEBIN, C. S.; MADEIRA, M. D.; YOKOYAMA-YASUNAKA, J. K. U.; MIGUEL, D. C.; ULIANA, S. R. B.; BENITEZ, D.; CERECETTO, H.; GONZALEZ, M.; DA ROSA, R. G.; EIFLER-LIMA, V. L. . Synthesis and in vitro activity of limonene derivatives against Leishmania and Trypanosoma. <strong>European Journal of Medicinal Chemistry</strong>, v. 45, pp 1524-8, 2010.</li>
    </ul>
    <ul type="disc">
        <li>64)	HOLUB, N.; JIANG, H.; PAIX�O, M. W.; TIBERI, C.; J�RGENSEN, K. A. . An Unexpected Michael-Aldol-Smiles-Rearrangement Sequence for the Synthesis of Versatile Optically Active Bicyclic Structures using Asymmetric Organocatalysis. <strong>Chemistry - A European Journal</strong>, v. 16, pp 4337-4346, 2010.</li>
    </ul>
    <ul type="disc">
        <li>65)	HOLZSCHUH, M. H.; GOSMANN, G.; SCHNEIDER, P. H.; SCHAPOVAL, E. E. S.; BASSANI, V. L. . Identification and stability of a new bichalcone in Achyrocline satureioides spray dried powder. <strong>Pharmazie</strong>, v. 65, pp 650-656, 2010.</li>
    </ul>
    <ul type="disc">
        <li>66)	HORN, A.; PARRILHA, G. L.; MELO, K. V.; FERNANDES, C.; HORNER, M.; VISENTIN, L. DO C.; SANTOS, J. A. S.; SANTOS, M. S.; ELEUTHERIO, E. C. A.; PEREIRA, M. D. . An Iron-Based Cytosolic Catalase and Superoxide Dismutase Mimic Complex. <strong>Inorganic Chemistry</strong>, v. 49, pp 1274-1276, 2010.</li>
    </ul>
    <ul type="disc">
        <li>67)	HUMERES, E.; SOUZA, E. P., DEBACHER, N. A. . The mechanisms of hydrolysis of N-alkyl O-arylthioncarbamate esters. <strong>Journal of Physical Organic Chemistry</strong>, v. 23, pp 915- 924, 2010.</li>
    </ul>
    <ul type="disc">
        <li>68)	 JIANG, H.; PAIX�O, M. W.; MONGE, D.; J�RGENSEN, K. A. . Acyl Phosphonates: Good Hydrogen Bond Acceptors and Ester/Amide Equivalents in Asymmetric Organocatalysis. <strong>Journal of American Chemical Society</strong>, v. 132, pp 2775-2783, 2010.</li>
    </ul>
    <ul type="disc">
        <li>69)	KHALAF, P. I.; SOUZA, I. G.; CARASEK, E.; DEBACHER, N. A. . Estudo da efici�ncia de degrada��o de tetracloreto de carbono por plasma t�rmico e caracteriza��o dos produtos formados. <strong>Qu�mica Nova</strong>, v. 33, pp 398 - 403, 2010.</li>
    </ul>
    <ul type="disc">
        <li>70)	KIRBY, A. J.; DAVIES, J. E.; FOX, D. J.; HODGSON, D. R. W.; GOETA, A. E.; LIMA, M. F.; PRIEBE, J. P.; SANTABALLA, J. A.; NOME, F. . Ammonia oxide makes up some 20% of an aqueous solution of hydroxylamine. <strong>Chemical Communications</strong>, v. 46, pp 1302-1304, 2010.  </li>
    </ul>
    <ul type="disc">
        <li>71)	LIMA JR, E.; DE BIASI, E.; VASQUEZ MANSILLA, M.; SALETA, M. E.; EFFENBERGER, F. B.; ROSSI, L. M.; COHEN, R.; RECHENBERG, H. R.; ZYSLER, R. D. . Surface effects in the magnetic properties of crystalline 3 nm ferrite nanoparticles chemically synthesized. <strong>Journal of Applied Physics</strong>, v. 108, pp 103919-1-103919-10, 2010.</li>
    </ul>
    <ul type="disc">
        <li>72)	LOPES, J. F.; ROCHA, W. R.; SANTOS, H. F.; ALMEIDA, W. B. . An Investigation of the BSSE Effect on the Evaluation of Ab Initio Interaction Energies for Cisplatin-Water Complexes. <strong>Journal of the Brazilian Chemical Society</strong>, v. 21, pp 887-896, 2010.</li>
    </ul>
    <ul type="disc">
        <li>73)	MARINI, V. G.; TORRI, E.; ZIMMERMANN, L. M.; MACHADO, V. G. . An anionic chromogenic chemosensor based on 4-(4-nitrobenzylideneamine)-2,6-diphenylphenol for selective detection of cyanide in acetonitrile water mixtures. <strong>ARKIVOC</strong>, v. 11, pp 146-162, 2010.</li>
    </ul>
    <ul type="disc">
        <li>74)	MARINI, V. G.; ZIMMERMANN, L. M.; MACHADO, V. G. . A simple and efficient anionic chromogenic chemosensor based on 2,4-dinitrodiphenylamine in dimethyl sulfoxide and in dimethyl sulfoxide water mixtures. <strong>Spectrochimica Acta. Part A - Molecular and Biomolecular Spectroscopy</strong>, v. 75, p 799-806, 2010.</li>
    </ul>
    <ul type="disc">
        <li>75)	MARINI, V. G.; ZIMMERMANN, L. M.; MACHADO, V. G. . Ensaios anal�ticos baseados em quimiossensores cromog�nicos e fluorog�nicos para a detec��o de cianeto. <strong>Orbital-The Electronic Journal of Chemistry</strong>, v. 2, pp 53-91, 2010.</li>
    </ul>
    <ul type="disc">
        <li>76)	MENEZES, F. G.; GALLARDO, H.; ZUCCO, C. . Recentes Aplica��es Sint�ticas de Compostos Org�nicos Tricloro(Bromo)Metila Substitu�dos. <strong>Qu�mica Nova</strong>, v. 33, pp 2233-2244, 2010.</li>
    </ul>
    <ul type="disc">
        <li>77)	MERTINS, O.; SCHNEIDER, P. H.; POHLMANN, A. R.; DA SILVEIRA, N. P. . Interaction between phospholipids bilayer and chitosan in liposomes investigated by P-31 NMR spectroscopy. <strong>Colloids and Surfaces B-Biointerfaces</strong>, v. 75, pp 294-9, 2010.</li>
    </ul>
    <ul type="disc">
        <li>78)	MIGNONI, M. L.; SOUZA, M. O.; PERGHER, S. B. C.; SOUZA, R. F.; BERNARDO-GUSMAO, K. . Nickel oligomerization catalysts heterogenized on zeolites obtained using ionic liquids as templates. <strong>Applied Catalysis A-General</strong>, v. 374, pp  26-30, 2010. </li>
    </ul>
    <ul type="disc">
        <li>79)	MIGOWSKI, P.; ZANCHET, D.; MACHADO, G.; GELESKY, M. A.; TEIXEIRA, S. R ; DUPONT, J. . Nanostructures in ionic liquids: correlation of iridium nanoparticles' size and shape with imidazolium salts' structural organization and catalytic properties. <strong>Physical Chemistry Chemical Physics</strong>, v. 12, pp 6826-33, 2010.</li>
    </ul>
    <ul type="disc">
        <li>80)	MILANI, M. A.; SOUZA, M. O.; SOUZA, R. F. . (NiPO)-O-boolean AND and [Cp2ZrCl2/MAO] as a versatile dual-function catalyst system for in situ polymerization of ethylene to linear low-density polyethylene (LLDPE). <strong>Catalysis Communications</strong>, v. 11, p 1094-7, 2010.</li>
    </ul>
    <ul type="disc">
        <li>81)	MONFETTE, S.; CRANE, A. K.; DUARTE SILVA, J. A.; FACEY, G. A.; SANTOS, E. N.; ARAUJO, M. H.; FOGG, D.E. . Monitoring ring-closing metathesis: Limitations on the utility of 1H NMR analysis. <strong>Inorganica Chimica Acta</strong>, v. 363, pp 481-486, 2010. </li>
    </ul>
    <ul type="disc">
        <li>82)	NANGOI, I. M.; KIYOHARA, P. K.; ROSSI, L. M. . Catalytic hydrodechlorination of chlorobenzene over supported palladium catalyst in buffered medium. <strong>Applied Catalysis. B - Environmental</strong>, v. 100, pp 42-46, 2010. </li>
    </ul>
    <ul type="disc">
        <li>83)	NARAYANAPERUMAL, S.; ALBERTO, E. E.; GUL, K.; RODRIGUES, O. E. D.; BRAGA, A. L. . Synthesis of Diorganyl Selenides Mediated by Zinc in Ionic Liquid. <strong>Journal of Organic Chemistry</strong>, v. 75, pp 3886 - 3889, 2010.</li>
    </ul>
    <ul type="disc">
        <li>84)	NARAYANAPERUMAL, S.; GUL, K.; KAWASOKO, C. Y.; SINGH, D.; DORNELLES, L.; RODRIGUES, O. E. D.; BRAGA, A. L. . Transition metal oxide nanopowder and ionic liquid: an efficient system for the synthesis of diorganyl selenides, selenocysteine and derivatives. <strong>Journal of the Brazilian Chemical Society</strong>, v. 21, pp 2079-2087, 2010.</li>
    </ul>
    <ul type="disc">
        <li>85)	NETO, B. A. D.; LAPIS, A. A. M.; MANCILHA, F. S.; BATISTA, E. L.; NETZ, P. A.; ROMINGER, F.; BASSO, L. A.; SANTOS, D. S.; DUPONT, J. . On the selective detection of duplex deoxyribonucleic acids by 2,1,3-benzothiadiazole fluorophores. <strong>Molecular Biosystems</strong>, v. 6, pp 967-75, 2010.</li>
    </ul>
    <ul type="disc">
        <li>86)	NETO, B. A. D.; LAPIS, A. A. M.; NETZ, P. A.; SPENCER, J.; DIAS, S. L. P.; TAMBORIM, S. M.; BASSO, L. A.; SANTOSE, D. S.; DUPONT, J. . Synthesis and Enzymatic Evaluation of the Guanosine Analogue 2-Amino-6-mercapto-7-methylpurine Ribonucleoside (MESG). Insights into the Phosphorolysis Reaction Mechanism based on the Blueprint Transition State: S(N)1 or S(N)2? <strong>Journal of The Brazilian Chemical Society</strong>, v. 21, pp 151-U61, 2010.  </li>
    </ul>
    <ul type="disc">
        <li>87)	NEVES, A. . Catalytic Promiscuity: Catecholase-like Activity and Hydrolytic DNA Cleavage. <strong>Journal of the Brazilian Chemical Society</strong>, v. 21, pp 1201-1212, 2010.</li>
    </ul>
    <ul type="disc">
        <li>88)	NIELSEN, M.; JACOBSEN, C. B.; HOLUB, N.; PAIX�O, M. W.; J�RGENSEN, K. A. . Asymmetric Organocatalysis with Sulfones. <strong>Angewandte Chemie International Edition</strong>, v. 49, pp 2668-2679, 2010.</li>
    </ul>
    <ul type="disc">
        <li>89)	NOME, F. . Special Issue of 10th Latin American Conference on Physical Organic Chemistry Preface. <strong>Journal of Physical Organic Chemistry</strong>, v. 23, pp 885-885, 2010.         </li>
    </ul>
    <ul type="disc">
        <li>90)	NOME, R. A.; SOUZA, A. J.; NOME, C. A.; SOUZA, B. S. ; NOME, F.; FIEDLER, H. D. . Interaction between an organic dye in water and sand packs in a flume system. <strong>Environmental Toxicology and Chemistry</strong>, v. 29, pp 2426-2431, 2010.</li>
    </ul>
    <ul type="disc">
        <li>91)	OLIVEIRA, F. F. D.; SANTOS, D. C. B. D.; LAPIS, A. A. M.; al., et . On the use of 2,1,3-benzothia diazole derivatives as selective live cell fluorescence imaging probes.  <strong>Bioorganic &amp; medicinal chemistry letters</strong>, v. 20, pp 6001-6007, 2010.</li>
    </ul>
    <ul type="disc">
        <li>92)	OLIVEIRA, L. L.; CAMPEDELLI, R. R.; BERGAMO, A. L.; DOS SANTOS, A. H. D. P.; CASAGRANDE, O. L. . Substituted Tridentate Pyrazolyl Ligands for Chromium and Nickel-Catalyzed Ethylene Oligomerization Reactions. Effect of Auxiliary Ligand on Activity and Selectivity. <strong>Journal of the Brazilian Chemical Society</strong>, v. 21, pp 1318-28, 2010.</li>
    </ul>
    <ul type="disc">
        <li>93)	OLIVEIRA, R. L.; KIYOHARA, P. K. ; ROSSI, L. M. . High performance magnetic separation of gold nanoparticles for catalytic oxidation of alcohols. <strong>Green Chemistry</strong>, v. 12, pp 144-149, 2010. </li>
    </ul>
    <ul type="disc">
        <li>94)	ORTH, E. S.; BRAND�O, T. A. S.; SOUZA, B. S.; PLIEGO, J. R.; VAZ, B. G.; EBERLIN, M. N.; KIRBY, A. J.; NOME, F. . Intramolecular Catalysis of Phosphodiester Hydrolysis by Two Imidazoles. <strong>Journal of the American Chemical Society</strong>, v. 132, pp 8513-8523, 2010.</li>
    </ul>
    <ul type="disc">
        <li>95)	PADILHA, J. C.; BASSO, J.; DA TRINDADE, L. G.; MARTINI, E. M. A.; SOUZA, M. O.; SOUZA, R. F. . Ionic liquids in proton exchange membrane fuel cells: Efficient systems for energy generation. <strong>Journal of Power Sources</strong>, v. 195, pp 6483-5, 2010.</li>
    </ul>
    <ul type="disc">
        <li>96)	PARREIRA, L. A.; MENINI, L.; SANTOS, J. C. DA C.; GUSEVSKAYA, E. V. . Palladium-catalyzed aerobic oxidation of naturally occurring allyl benzenes as a route to valuable fragrance and pharmaceutical compounds. <strong>Advanced Synthesis &amp; Catalysis</strong>, v. 352, pp 1533-1538, 2010.</li>
    </ul>
    <ul type="disc">
        <li>97)	PARRILHA, G. L.; FERREIRA, S. DA S.; FERNANDES, C.; SILVA, G. C.; CARVALHO, N. M. F.; ANTUNES, O. A. C.; DRAGO, V.; BORTOLUZZI, A. J; HORN JR., A. . Properties of (&#956;-Oxo)di-iron Complexes and Catalytic Activity Toward Cyclohexane Oxidation. <strong>Journal of the Brazilian Chemical Society</strong>, v. 21, pp 603 - 613, 2010.</li>
    </ul>
    <ul type="disc">
        <li>98)	PERALTA, R. A.; BORTOLUZZI, A. J.; BRANDAO, T. A. S.; SZPOGANICZ, B.; CASTELLANO, E. E.; DE OLIVEIRA, M. B.; SEVERINO, P. C.; TERENZI, H.; NEVES, A. . Catecholase and DNase activities of copper(II) complexes containing phenolate-type ligands. <strong>Journal of Physical Organic Chemistry</strong>, v. 23, pp 1000 - 1013, 2010.</li>
    </ul>
    <ul type="disc">
        <li>99)	PERALTA, R. A.; BORTOLUZZI, A. J.; SOUZA, B.; al., et . Electronic Structure and Spectro-Structural Correlations of (FeZnII)-Zn-III Biomimetics for Purple Acid Phosphatases: Relevance to DNA Cleavage and Cytotoxic Activity. <strong>Inorganic chemistry</strong>, v. 49, pp 11421-11438, 2010.</li>
    </ul>
    <ul type="disc">
        <li>100)	PEREIRA-MAIA, E.; SILVA, P. P.; ALMEIDA, W B; SANTOS, H. F.; MARCIAL, B. L.; RUGGIERO, R.; GUERRA, W. . Tetraciclinas e glicilciclinas: Uma vis�o geral. <strong>Qu�mica Nova</strong>, v. 33, pp 700-706, 2010. </li>
    </ul>
    <ul type="disc">
        <li>101)	PILISS�O, C.; CARVALHO, P. O; NASCIMENTO, M.G. . Potencial Application Of Native Lipases In The Resolution Of (Rs)-Phenylethylamine. <strong>Journal of Brazilian Chemical Society</strong>, v. 21, pp 973-977, 2010.</li>
    </ul>
    <ul type="disc">
        <li>102)	PIOVEZAN, C.;  JOVITO, R.; BORTOLUZZI, A. J.; TERENZI, H.; FISCHER, F. L.;  SEVERINO, P. C; PICH, C. T.; AZZOLINI, G. G.; PERALTA, R. A.; ROSSI, L. M.; NEVES, A. . Heterodinuclear FeIIIZnII Bioinspired Complex Supported on 3-aminopropyl Silica. Efficient Hydrolysis of Phosphate Diester Bonds. <strong>Inorganic Chemistry</strong>, v. 49, pp 2580-2582, 2010. </li>
    </ul>
    <ul type="disc">
        <li>103)	PIZZUTI, L.; MARTINS, P. L. G.; RIBEIRO, B. A.; QUINA, F. H.; PINTO, E.; FLORES, A. F. C.; VENZKE, D.; PEREIRA, C. M. P. . Efficient sonochemical synthesis of novel 3,5-diaryl-4,5-dihydro-1H-pyrazole-1-carboximidamides. <strong>Ultrasonics Sonochemistry</strong>, v. 17, pp 34-37, 2010.</li>
    </ul>
    <ul type="disc">
        <li>104)	POSSIDONIO, S.; FIDALE, L. C.; EL SEOUD, O. A. . Microwave-Assisted Derivatization of Cellulose in an Ionic Liquid: An Efficient, Expedient Synthesis of Simple and Mixed Carboxylic Esters. <strong>Journal of Polymer Science - A</strong>, v. 48, pp 134-143, 2010.</li>
    </ul>
    <ul type="disc">
        <li>105)	PRECHTL, M. H. G.; SCHOLTEN, J. D.; DUPONT, J. . Carbon-Carbon Cross Coupling Reactions in Ionic Liquids Catalysed by Palladium Metal Nanoparticles. <strong>Molecules</strong>, v. 15, pp 3441-61, 2010.</li>
    </ul>
    <ul type="disc">
        <li>106)	PRIEBE, J. P.; SOUZA, B. S.; MICKE, G. A.; COSTA, A. C. O.; FIEDLER, H. D.; BUNTON, C. A.; NOME, F. . Anion-Specific Binding to n-Hexadecyl Phosphorylcholine Micelles. <strong>Langmuir</strong>, v. 26, pp 1008-1012, 2010.  </li>
    </ul>
    <ul type="disc">
        <li>107)	RAMBO, R. S.; SCHNEIDER, P. H. . Thiazolidine-based organocatalysts for a highly enantioselective direct aldol reaction. <strong>Tetrahedron-Asymmetry</strong>, v. 21, pp 2254-2257, 2010.</li>
    </ul>
    <ul type="disc">
        <li>108)	RAMPON, D. S.; RODEMBUSCH, F. S.; GONCALVES, P. F. B.; LOUREGA, R. V.; MERLO, A. A.; SCHNEIDER, P. H. . An Evaluation of the Chalcogen Atom Effect on the Mesomorphic and Electronic Properties in a New Homologous Series of Chalcogeno Esters. <strong>Journal of Brazilian Chemical Society</strong>, v. 21, pp 2100-2107, 2010.</li>
    </ul>
    <ul type="disc">
        <li>109)	RAMPON, D. S.; RODEMBUSCH, F. S.; SCHNEIDER, J. M. F. M.; BECHTOLD, I. H.; GONCALVES, P. F. B.; MERLO, A. A.; SCHNEIDER, P. H. . Novel selenoesters fluorescent liquid crystalline exhibiting a rich phase polymorphism.  <strong>Journal of Materials Chemistry</strong>, v. 20, pp 715-722, 2010.</li>
    </ul>
    <ul type="disc">
        <li>110)	ROCHA, D. P.; PINTO, G. F.; RUGGIERO, R.; OLIVEIRA, C. A. DE; GUERRA, W.; FONTES, A. P. S.; TAVARES, T. T.; MARZANO, I. M.; PEREIRA-MAIA, E. C. . Coordena��o de Metais a Antibi�ticos como uma Estrat�gia de Combate � Resist�ncia Bacteriana. <strong>Qu�mica Nova</strong>, v. 34, pp 111-118, 2010.</li>
    </ul>
    <ul type="disc">
        <li>111)	ROCHA, K. A. S.; RODRIGUES, N. V. S.; KOZHEVNIKOV, I. V.; GUSEVSKAYA, E. V. . Heteropoly acid catalysts in the valorization of the essential oils: acetoxylation of caryophyllene. <strong>Applied Catalysis. A - General</strong>, v.  374, pp  87-94, 2010.  </li>
    </ul>
    <ul type="disc">
        <li>112)	RODRIGUES, O. E. D.; SOUZA, D.; SOARES, L. C.; DORNELLES, L.; BURROW, R. A.; APPELT, H. R.; ALVES, C. F.; ALVES, D.; BRAGA, A. L. . Stereoselective synthesis of selenosteroids. <strong>Tetrahedron Letters</strong>, v. 51, pp 2237-2240, 2010.</li>
    </ul>
    <ul type="disc">
        <li>113)	ROSA, R. M.; GUECHEVA, T. N.; OLIVEIRA, I. M. DE.; HENRIQUES, J. A. P.; BRAGA, A. L. . Genetic toxicity of three symmetrical diselenides in yeast. <strong>Journal of the Brazilian Chemical Society</strong>, v. 21, pp 2119 - 2124, 2010.</li>
    </ul>
    <ul type="disc">
        <li>114)	ROS�RIO, A. R.; SCHUMACHER, R. F.; GAY, B. M.; MENEZES, P. H.; ZENI, G. . Synthesis and Reactivity of 3-Alkynyldihydroselenophene Derivatives. <strong>European Journal of Organic Chemistry</strong>, v. 29, pp 5601-5606, 2010.</li>
    </ul>
    <ul type="disc">
        <li>115)	SABADINI, E.; FRANCISCO, K. R.; BOUTEILLER, L. . Bis-Urea-Based Supramolecular Polymer: The First Self-Assembled Drag Reducer for Hydrocarbon Solvents. <strong>Langmuir</strong>, v.  26, pp 1482-1486, 2010.  </li>
    </ul>
    <ul type="disc">
        <li>116)	S�ENZ, L. A.; SEIBERT, E. L.; ZANETTE, J.; FIEDLER, H. D.; CURTIUS, A. J.; FERREIRA, J. F.; ALMEIDA, E. A. DE; MARQUES, M. R. F.; BAINY, A. C. D. . Biochemical biomarkers and metals in Perna perna mussels from mariculture zones of Santa Catarina, Brazil. <strong>Ecotoxicology and Environmental Safety</strong>, v. 73, pp 796-804, 2010.</li>
    </ul>
    <ul type="disc">
        <li>117)	SANTOS, A. L. F.; MARTINS, D. U.; IHA, O. K.; al., et . Agro-industrial residues as low-price feedstock for diesel-like fuel production by thermal cracking. <strong>Bioresource technology</strong>, v. 101, pp 6157-6162, 2010. </li>
    </ul>
    <ul type="disc">
        <li>118)	SATNAMI, M. L.; DHRITLAHRE, S.; NAGWANSHI, R.; al., et . Nucleophilic Attack of Salicylhydroxamate Ion at C=O and P=O Centers in Cationic Micellar Media. <strong>Journal of Physical Chemistry C</strong>, v. 114, pp 16759-16765, 2010.</li>
    </ul>
    <ul type="disc">
        <li>119)	SATO, B. M.; OLIVEIRA, C. G.; MARTINS, C. T.; EL SEOUD, O. A. . Thermo-solvatochromism in binary mixtures of water and ionic liquids: on the relative importance of solvophobic interactions. <strong>Physical Chemistry Chemical Physics</strong>, v. 12, pp 1764-1771, 2010.  </li>
    </ul>
    <ul type="disc">
        <li>120)	 SCAPINI, P.; FIGUEROA, C. A.; AMORIM, C. L. G.; MACHADO, G.; MAULER, R. S.; CRESPO, J. S.; OLIVEIRA, R. V. B. . Thermal and morphological properties of high-density polyethylene/ethylene-vinyl acetate poly composites with polyhedral oligomeric silsesquioxane nanostructure. <strong>Polymer International</strong>, v. 59, pp 175-180, 2010.  </li>
    </ul>
    <ul type="disc">
        <li>121)	SCHENEIDER, C. C.; MANARIN, F.; PANATIERI, R. B.; BARROS, O. S. DO R.; ZENI, G. . PhSeBr-Catalyzed Selective Addition of Thiols to alpha,beta-Unsaturated Carbonyl Compounds: Regioselective Synthesis of Thioacetals vs. beta-Mercapto Ketones. <strong>Journal of the Brazilian Chemical Society</strong>, v. 21, pp 2088-2092, 2010.</li>
    </ul>
    <ul type="disc">
        <li>122)	SCHNEIDER, C. C.; CALDEIRA, H.; GAY, B. M.; BACK, D. F.; ZENI, G. . Transmetalation of Z-Telluroenynes: Stereloselective Synthesis of Z-Enynols and Their Application in Palladium-Catalyzed Cyclization. <strong>Organic Letters</strong>, v. 12, pp 936-939, 2010.  </li>
    </ul>
    <ul type="disc">
        <li>123)	SCHOLTEN, J. D.; PRECHTL, M. H. G.; DUPONT, J. . Decomposition of Formic Acid Catalyzed by a Phosphine-Free Ruthenium Complex in a Task-Specific Ionic Liquid. <strong>Chemcatchem</strong>, v. 2, pp 1265-70, 2010.</li>
    </ul>
    <ul type="disc">
        <li>124)	SCHULZ, G. A. S.; COMIN, E.; SOUZA, R. F. . Hydrogenation of NBR Latex by Diimide Reduction Using Selenium Catalysts. <strong>Journal of Applied Polymer Science</strong>, v. 115, pp 1390-1394, 2010.  </li>
    </ul>
    <ul type="disc">
        <li>125)	SCHUMACHER, R. F.; ROS�RIO, A. R.; SOUZA, A. C. G.; MENEZES, P. H.; ZENI, G. . Synthesis of 2,3-Dihydroselenophene and Selenophene Derivatives by Electrophilic Cyclization of Homopropargyl Selenides. <strong>Organic Letters</strong>, v. 12, pp 1952-1955, 2010.</li>
    </ul>
    <ul type="disc">
        <li>126)	SCHWAB, R. S.; SOARES, L. C.; DORNELLES, L.; RODRIGUES, O. E. D.; PAIX�O, M. W.; GODOI, M.; BRAGA, A. L. . Chiral Chalcogen Peptides as Ligands for the Catalytic Enantioselective Aryl Transfer Reaction to Aldehydes. <strong>European Journal of Organic Chemistry</strong>, v. 19, pp 3574-3578, 2010.</li>
    </ul>
    <ul type="disc">
        <li>127)	SEHNEM, J. A.; MOLANI, P.; NASCIMENTO, V.;  ANDRADE, L. H.; DORNELES, L.; BRAGA, A. L. . Synthesis of new fluorous modular chiral ligand derivatives from amino alcohols and application in enantioselective carbon-carbon bond-forming alkylation reactions. <strong>Tetrahedron Asymmetry</strong>, v. 21, pp 997-1003, 2010.</li>
    </ul>
    <ul type="disc">
        <li>128)	SILVA, A. F; FIEDLER, H. D; NOME, F. . Ionic Quenching of Naphthalene Fluorescence in Sodium Dodecyl Sulfate Micelles. <strong>Journal of Physical Chemistry A</strong>, v. 115, pp 2509-2514, 2010.</li>
    </ul>
    <ul type="disc">
        <li>129)	SILVA, D.; CASTILHO JR, A. B.; ROHERS, F.; DEBACHER, N. A. . Caracteriza��o F�sico-Qu�mica e Microestrutural de Conchas de Moluscos Bivalves Provenientes de Cultivos Da Regi�o Litor�nea da Ilha de Santa Catarina. <strong>Qu�mica Nova</strong>, v. 33, pp 1053-1058, 2010.</li>
    </ul>
    <ul type="disc">
        <li>130)	SILVA, F. A. N.; PIZZUTI, L.; QUINA, F. H.; SOUZA, S. P.; ROSALES, P. F.; SIQUEIRA, G. M.; PEREIRA, C. M. P.; BARROS, S. B. M.; RIVELLI, D. P. . Antioxidant Capacity of 2-(3,5-diaryl-4,5-dihydro-1H-pyrazol-1-yl)-4-phenylthiazoles. <strong>Letters in Drug Design & Discovery</strong>, v. 7, pp 657-660, 2010.</li>
    </ul>
    <ul type="disc">
        <li>131)	SILVA, J. C. S. DA; DIAS, R. P.; ALMEIDA, W. B. DE; ROCHA, W. R. . DFT Study of the Full Catalytic Cycle for the Propene Hydroformylation Catalyzed by a Heterobimetallic HPt(SnCl3)(PH3)2 Model Catalyst. <strong>Journal of Computational Chemistry</strong>, v. 31, pp 1986, 2010.</li>
    </ul>
    <ul type="disc">
        <li>132)	SILVA, P. A.; JACOBI, M. M.; SCHNEIDER, L. K.; BARBOSA, R. V.; COUTINHO, P. A.; OLIVEIRA, R. V. B.; MAULER, R. S. . SBS nanocomposites as toughening agent for polypropylene. <strong>Polymer Bulletin</strong>, v. 64, pp 245-57, 2010.</li>
    </ul>
    <ul type="disc">
        <li>133)	SILVA, P. P.; PAULA, F. C. S. DE; GUERRA, W; SILVEIRA, J. N.; BOTELHO, F. V.; VIEIRA, L. Q.; BORTOLOTTO, T.; FISCHER, F. L.; BUSSI, G.; TERENZI, H. I.; PEREIRA-MAIA, E. C. . Platinum(II) Compounds of Tetracyclines as Potential Anticancer Agents: Cytotoxicity, Uptake and Interactions with DNA. <strong>Journal of Brazilian Chemical Society</strong>, v. 21, pp 1237-1246, 2010.</li>
    </ul>
    <ul type="disc">
        <li>134)	SILVA, R. O.; NEVES, F. R. A. W.; AZEVEDO, R.; SRIVASTAVA, R. M.; GALLARDO, H. . Complete 1H and 13C NMR signal assignments and chemical shift calculations of four 1,2,4-oxadiazole-based light-emitting liquid crystals. <strong>Structural Chemistry</strong>, v. 21, pp 485-494, 2010.  </li>
    </ul>
    <ul type="disc">
        <li>135)	SILVA, R. P.; MAULER, R. S.; DE OLIVEIRA, R. V. B.; SALLES, C. A. . Evaluation of Mechanical-Thermal Properties and Morphological in PVC Nanocomposites. <strong>Polimeros - Ci�ncia e Tecnologia</strong>, v. 20, pp 46-50, 2010.</li>
    </ul>
    <ul type="disc">
        <li>136)	SILVA, V. D.; STAMBUCK, B. U.; NASCIMENTO, M. G. . Efficient Chemoselective Biohydrogenation Of 1,3-Diaryl-2-Propen-1-Ones Catalyzed By Saccharomyces Cerevisiae Yeasts In Biphasic System. J.  <strong>Journal of Molecular Catalysis B: Enzymatic</strong>, v. 63, pp 157-163, 2010.</li>
    </ul>
    <ul type="disc">
        <li>137)	SIMAS, E. R.; GEHLEN, M. H.; PINTO, M. F. S.; SIQUEIRA, J.; MISOGUTI, L. . Intrachain energy migration to weak charge-transfer state in polyfluorene end-capped with naphthalimide derivative. <strong>Journal of Physical Chemistry A</strong>, v. 114, pp 12384-12390, 2010.</li>
    </ul>
    <ul type="disc">
        <li>138)	SINGH, D.; DEOBALD, A; CAMARGO, L. R. S.; TABARELLI, G.; RODRIGUES, O. E. D.; BRAGA, A. L. . An Efficient One-Pot Synthesis of Symmetrical Diselenides or Ditellurides from Halides with cuo Nanopowder/Se or Te/Base. <strong>Organic Letters</strong>, v. 12, pp 3288-3291, 2010.</li>
    </ul>
    <ul type="disc">
        <li>139)	SINGH, D.; GALETTO, F. Z.; SOARES, L. C.; RODRIGUES, O. E. D.; BRAGA, A. L. . Metal-Free Air Oxidation of Thiols in Recyclable Ionic Liquid: A Simple and Efficient Method for the Synthesis of Disulfides. <strong>European Journal of Organic Chemistry</strong>, v. 14, pp 2661-2665, 2010.</li>
    </ul>
    <ul type="disc">
        <li>140)	SINGH, D.; NARAYANAPERUMAL, S.; GUL, K.; GODOI, M.; RODRIGUES, O. E. D.; BRAGA, A. L. . Efficient synthesis of selenoesters from acyl chlorides mediated by CuO nanopowder in ionic liquid. <strong>Green Chemistry</strong>, v. 12, pp 957, 2010.</li>
    </ul>
    <ul type="disc">
        <li>141)	SOUZA, B. DE; BORTOLUZZI, A. J.; BORTOLOTTO, T.; FISCHER, F. L.; TERENZI, H.; FEREIRA, D. E. C.; ROCHA, W. R.; NEVES, A. . DNA Photonuclease Activity of Four New Copper(II) Complexes Under UV and Red Light: Theoretical/Experimental Correlations with Active Species Generation. <strong>Dalton Transactions</strong>, v. 39, pp 2027, 2010.</li>
    </ul>
    <ul type="disc">
        <li>142)	SOUZA, B. S.; VITTO, R.; NOME, F.; al., et . 3-Acetoxy-2-naphthoic acid. <strong>Acta Crystallographica Section E</strong>, v. 66, pp O2848-U471, 2010.</li>
    </ul>
    <ul type="disc">
        <li>143)	SOUZA, B. S; NOME, F. . Importance of Equilibrium Fluctuations between Most Stable Conformers in the Control of the Reaction Mechanism. <strong>Journal of Organic Chemistry</strong>, v. 75, pp 7186-7193, 2010.</li>
    </ul>
    <ul type="disc">
        <li>144)	SOUZA, B.; XAVIER, F. R.; PERALTA, R. A.; BORTOLUZZI, A. J.; CONTE, G.; GALLARDO, H.; FISCHER, F. L.; BUSSI, G.; TERENZI, H.; NEVES, A. . Oxygen-independent photonuclease activity of a new iron(II) complex. <strong>Chemical Communications</strong>, v. 46, pp 3375, 2010.</li>
    </ul>
    <ul type="disc">
        <li>145)	SOUZA, M. O.; RODRIGUES, L. R.; GAUVIN, R. M.; SOUZA, R. F.; PASTORE, H. O.; GENGEMBRE, L.; RUIZ, J. A. C.; GALLO, J. M. R.; MILANESI, T. S.; MILANI, M. A.  . Support effect in ethylene oligomerization mediated by heterogenized nickel catalysts. <strong>Catalysis Communications</strong>, v. 11, pp 597-600, 2010. </li>
    </ul>
    <ul type="disc">
        <li>146)	SPERANCA, A.; GODOI, B.; SOUZA, A. C. G.; ZENI, G. . 3-Iodo-4-chalcogen-2H-benzopyran as a convenient precursor for the sonogashira cross-coupling: synthesis of 3-alkynyl-4-chalcogen-2H-benzopyrans. <strong>Tetrahedron Letters</strong>, v. 51, pp 36-39, 2010. </li>
    </ul>
    <ul type="disc">
        <li>147)	STEIN, A. L.; ROCHA, J.; MENEZES, P. H.; ZENI, G. . Synthesis of Fused 4-Iodoselenophene[2,3-b]thiophenes by Electrophilic Cyclization of 3-Alkynylthiophenes. <strong>European Journal of Organic Chemistry</strong>, v. 4, pp  705-710, 2010.  </li>
    </ul>
    <ul type="disc">
        <li>148)	TABARELLI, G.; ALBERTO, E. E.; DEOBALD, A. M.; MARIN, G.; RODRIGUES, O. E. D.; DORNELLES, L.; BRAGA, A. L. . Ionic liquid: an efficient and reusable media for seleno- and thioester synthesis promoted by indium. <strong>Tetrahedron Letters. </strong>, v. 51, pp 5728 - 5731, 2010.</li>
    </ul>
    <ul type="disc">
        <li>149)	TADA, D. B.; ROSSI, L. M.; LEITE, C. A. P.; ITRI, R.; BAPTISTA, M. S. . Nanoparticle platform to modulate reaction mechanism of phenothiazine photosensitizers.  <strong>Journal of Nanoscience and Nanotechnology</strong>, v. 10, pp 3100-3108, 2010. </li>
    </ul>
    <ul type="disc">
        <li>150)	TAVARES, A.; RITTER, O. M. S.; VASCONCELOS, U. B.; ARRUDA, B. C.; SCHRADER, A.; SCHNEIDER, P. H.; MERLO, A. A. . Synthesis of liquid-crystalline 3,5-diarylisoxazolines. <strong>Liquid Crystals</strong>, v. 37, pp 159-169, 2010.  </li>
    </ul>
    <ul type="disc">
        <li>151)	 THIELE, D.; DE SOUZA, R. F. . Oligomerization of Ethylene Catalyzed by Iron and Cobalt in Organoaluminate Dialkylimidazolium Ionic Liquids.  <strong>Catalysis Letters</strong>, v. 138, pp 50-55, 2010.</li>
    </ul>
    <ul type="disc">
        <li>152)	 TIEKINK, E. R. T.; WARDELL, J. L.; FERNANDES, C.; HORN, A.; SKAKLE, J. M. S. . &#956;-Acetato-bis(&#956;-2-[(3-chloro-2-hydroxypropyl)(2-pyridylmethyl)amino]methylphenolato)dinickel(II) chloride. <strong>Acta Crystallographica. Section E</strong>, v. 66, pp M566-M567, 2010.</li>
    </ul>
    <ul type="disc">
        <li>153)	TONDO, D. W.; LEOPOLDINO, E. C.; SOUZA, B. S.; MICKE, G. A.; COSTA, A. C. O.; FIEDLER, H. D.; BUNTON, C. A.; NOME, F. . Synthesis of a New Zwitterionic Surfactant Containing an Imidazolium Ring. Evaluating the Chameleon-like Behavior of Zwitterionic Micelles. <strong>Langmuir</strong>, v. 26, pp 15754-15760, 2010.</li>
    </ul>
    <ul type="disc">
        <li>154)	VENZKE, D.; FLORES, A. F. C.; QUINA, F. H.; PIZZUTI, L.; PEREIRA, C. M. P. . Ultrasound promoted greener synthesis of 2-(3,5-diaryl-4,5-dihydro-1H-pyrazol-1-yl)-4-phenylthiazoles.<strong>Ultrasonics Sonochemistry</strong>, v. 18, pp 370-374, 2010.</li>
    </ul>
    <ul type="disc">
        <li>155)	VIANNA, M. M. G. R.; DWECK, J.; QUINA, F. H.; CARVALHO, F. M. S.; NASCIMENTO, C. A. O. . Toluene and naphthalene sorption by iron oxide/clay composites. <strong>Journal of Thermal Analysis and Calorimetry</strong>, v. 101, pp 887-892, 2010.</li>
    </ul>
    <ul type="disc">
        <li>156)	VIEIRA, C. G.; SILVA, J. G. DA; PENNA, C. A. A.; SANTOS, E. N. DOS; GUSEVSKAYA, E. V. . Tandem  Hydroformylation-acetalization of para-menthenic terpenes under non-acidic conditions. <strong>Applied Catalysis - A</strong>, v. 380, pp 125-132, 2010.</li>
    </ul>
    <ul type="disc">
        <li>157)	WENDER, H.; DE OLIVEIRA, L. F.; FEIL, A. F.; LISSNER, E.; MIGOWSKI, P.; MENEGHETTI, M. R.; TEIXEIRA, S. R.; DUPONT, J. . Synthesis of gold nanoparticles in a biocompatible fluid from sputtering deposition onto castor oil.  <strong>Chemical Communications</strong>, v. 46, p. 7019-21, 2010.</li>
    </ul>
    <ul type="disc">
        <li>158)	 WENDER, H.; DE OLIVEIRA, L. F.; MIGOWSKI, P.; FEIL, A. F.; LISSNER, E.; PRECHTL, M. H. G.; TEIXEIRA, S. R.; DUPONT, J. . Ionic Liquid Surface Composition Controls the Size of Gold Nanoparticles Prepared by Sputtering Deposition. <strong>Journal of Physical Chemistry C</strong>, v. 114, pp 11764-11768, 2010.</li>
    </ul>
    <ul type="disc">
        <li>159)	WESTPHAL, E.; BECHTOLD, I. H.; GALLARDO, H. . Synthesis and Optical/ Thermal Behavior of New Azo Photoisomerizable Discotic Liquid Crystals. <strong>Macromolecules</strong>, v. 43, pp 1319-1328, 2010.  </li>
    </ul>
    <ul type="disc">
        <li>160)	ZANTA, C. L. P. S.; FRIEDRICH, L. C.; MACHULEK JR, A.; HIGA, K. M.; QUINA, F. H. . Surfactant Degradation by a Catechol-Driven Fenton Reaction. <strong>Journal of Hazardous Materials</strong>, v. 178, pp 258-263, 2010. </li>
    </ul>
    <ul type="disc">
        <li>161)	 ZIMMERMANN, L. M.; SILVA, A. F.; MEDEIROS, M.; BRUCH, J.; SOUZA, A. J.; NOME, R. A.; FIEDLER, H. D.; NOME, F.K. . Quantitative Treatment of Magnesium Ion Adsorption at the &#947;-AlO Water Interface. <strong>Journal of Physical Chemistry C</strong>, v. 114, pp 15037-15083, 2010.</li>
    </ul>
"""

soup = BeautifulSoup(html, "html.parser")
text_list = soup.find_all('li')
link_list = soup.find_all('a')

json_file = []

while len(link_list) < len(text_list):
    link_list.append(BeautifulSoup('<a href="">Clique aqui</a>', "html.parser").find_all('a')[0])

for text, link in list(zip(text_list, link_list)):
    artigo = {}
    text = text.text
    link = link.get('href')
    #print("TEXTO: %s\nLINK: %s\n" % (text, link))

    text = text[:][4:]
    pesq, info = text.split(" . ")   
    #print("pesq: %s\ninfo: %s\n" % (pesq, info)) 

    pesq_list = pesq.split("; ")
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
    artigo["ano"] = int(info[3].replace('.', ''))
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
with open('jsonForScript.json', 'w', encoding='utf8') as file:
    json.dump(json_file, file, ensure_ascii=False)