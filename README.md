# Ocean Protein Portal - Data File Templates #

Data file templates for contributing data to the Ocean Protein Portal (V 1.1) https://proteinportal.whoi.edu/.

## Creating an Ocean Protein Portal Data Submission

Data files and metadata should be submitted to the [Biological and Chemical Oceanography Data Management Office (BCO-DMO)](https://www.bco-dmo.org/).  Your data will be served from a Dataset Landing Page at BCO-DMO in addition to being imported into the Ocean Protein Portal.

If you have any questions about submitting data please Contact Us @ contact@oceanproteinportal.org or info@bco-dmo.org.

## Steps ##

### Format the data ###

Format your data according to the following templates.

Field names as a csv file:
* Protein Spectral Counts [[template](tabular/TEMPLATE_Protein-Spectral-Counts.csv)] _(csv)_
* FASTA of Protein Identifications (see more [about FASTA format at NCBI](https://blast.ncbi.nlm.nih.gov/doc/blast-topics/#fasta) )
* Peptide Spectral Counts [[template](tabular/TEMPLATE_Peptide-Spectral-Counts.csv)] _(csv)_

Field descriptions, units, types, and requirements:
* [Protein Spectral Counts](#protein-spectral-count-field-names-descriptions-units)
* Protein FASTA file
* [Peptide Spectral Counts](#peptide-spectral-count-field-names-descriptions-units)

Formatting instructions:
* Include all data fields labeled as "required" in your data.
* Use the OPP templates column names in your data files exactly.
* Protein identifiers used in your FASTA file should match the identifiers in your spectral count data.
* Ensure that your data are **processed, QA/QC’ed and research ready**. 
* Check that your data are compliant with the types defined in the template (e.g. best_protein_id_probability is a float so shouldn’t be a percent or include the % symbol in the value).
* You can include additional columns not defined in the template.  

### Submit your data files and metadata ###

#### Make a BCO-DMO dataset submission ####

* Go to https://submit.bco-dmo.org/ and choose "Submit a New Dataset." 
* Complete the metadata for your dataset and upload your files.
**  This includes a section to document your "Parameters" meaning column names, descriptions, and units in your protein and peptide data tables. You can download a copy of the template column names, descriptions and units csv files and modify them as needed so they correctly describe your particular data. You can upload these parameter description files to the "Files" section of your submission, or include them as text in the "Parameters" section.
* [Protein spectral count field names, descriptions, units](tabular/TEMPLATE_Protein_README.csv) (csv)
* [Peptide spectral count field names, descriptions, units](tabular/TEMPLATE_Peptide_README.csv) (csv)

**Make sure to include in your column descriptions:**
* The **time zone** of the date_y-m-d and time_h-m-s columns.  
* Include any missing data identifiers used in your data (e.g. NA, nd, NaN, -999)
* For any cell that can store multiple values (e.g. other_protein_ids), please notify us of the string which identifies the delimiter between each value.

#### What do I do if I need to update my dataset to a new version?

* Please email info@bco-dmo.org explaining you'd like to update data that is a part of the Ocean Protein Portal.
* Provide the information and files described here: https://bcodmo.gitbook.io/how-to/contribute/updating-a-dataset. 

#### BCO-DMO submission resources:

If you need help preparing or submitting your dataset(s), you can reach out to us at info@bco-dmo.org.  In your email, indicate that you would like the dataset included in the Ocean Protein Portal.

* Submission tool FAQs: https://bcodmo.gitbook.io/how-to/submission-tool-faqs
* Submitting data with the Submission Tool (includes walkthrough): https://bcodmo.gitbook.io/how-to/contribute/submitting-data-with-submission-tool

### What happens after I submit data?  ##

* You will receive an immediate automated message confirming BCO-DMO received your data submission and it is "Under Review."  
** If you do not see this email check your spam filter to allow mail from (bcodmo.bot@gmail.com and info@bco-dmo.org)
* BCO-DMO will review your data submission and send you an email within 48hours from info@bco-dmo.org.  That email will confirm BCO-DMO accepted the submission or whether additional information or files are needed. If you don't already have a project registered at BCO-DMO we may ask you to "Register a Project" at submit.bco-dmo.org.
* BCO-DMO will add an additional column ISO_DateTime_UTC (in UTC time zone) to your tables if it is not already included.  BCO-DMO uses the ISO 8601 datetime with timezone format "%Y-%m-%dT%H:%M(:%S)Z" AKA "YYYY-MM-DDThh:mm(:ss)Z" .
* Your dataset will be ingested into the Ocean Protein Portal and will have public dataset pages at BCO-DMO containing the information you provided along with your data submission.
* You will be sent links to review draft dataset pages ahead of public release at BCO-DMO.  We will need your final review of these draft pages.
* A Digital Object Identifier (DOI) will be assigned to your datasets.

If you have any questions about submitting data please contact **Contact Us @ [contact@oceanproteinportal.org](mailto:contact@oceanproteinportal.org)** or [info@bco-dmo.org](info@bco-dmo.org),

## Protein Spectral Count Field Names, Descriptions, Units ##
(_[as CSV](https://github.com/oceanproteinportal/data-file-templates/raw/master/tabular/TEMPLATE_Protein_README.csv)_)

| protein spectral count fields | Definition | required, recommended or optional | data type | units | format | multi-valued data cell? | relationships between files | example |
|-------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------|-----------|-----------------|------------|-------------------------|---------------------------------------------------------|-----------------------------------------|
| sample_id | Identifies the sample associated with this annotation| required | string | n/a | | no | | st6_200m_CID |
| cruise_id | Identifies the cruise on which collection occurred | required | string | n/a | | no | | KM1128 |
| station_id | Identifies the station for the location this sample was taken | required| string | n/a | | no | | 6 |
| latitude_dd | The latitude at the station in decimal degrees (-90 to 90) | required| float | decimal degrees | | no | | 17 |
| longitude_dd | The longitude at the station in decimal degrees (-180 to 180) | required| float | decimal degrees | | no | | -154.4 |
| depth_m | The depth in meters at which the sample as taken | required| float | meters| | no | | 200 |
| date_y-m-d | The date of sample collection| required| string | n/a | yyyy-mm-dd | no | | 2011-10-17 |
| time_h-m-s | The local time of sample collection. Hour and minutes should be provided. Seconds optional | recommended | string | n/a | hh:mm[:ss] | no | | 23:30 |
| minimum_filter_size_microns | Minimum size of the collection filter in microns | required| float | microns | | no | | 0.2 |
| maximum_filter_size_microns | Maximum size of the collection filter in microns | required| float | microns | | no | | 3 |
| protein_id | An identifier that uniquely identifies this protein within this dataset and the FASTA file.| required| string | n/a | | no | The protein identifier in the FASTA file| NODE_+1234.5678 |
| protein_name | A name identifying this protein| required| string | n/a | | no | | short-chain dehydrogenase/reductase SDR |
| spectral_count | The spectral count | required| integer | n/a | | no | | 2 |
| molecular_weight_kDa | The molecular weight in kilo-Daltons of the sample | optional | float | kDa | | no | | 45239.7 |
| ncbi_id | The NCBI identifier. | optional | string | n/a | | no | | 479434|
| ncbi_name | The name as it corresponds to the preceding NCBI identifier| optional | string | n/a | | no | | Sphaerobacter thermophilus DSM 20745|
| kegg_id | The Kegg Orthology Entry identifier for the best Kegg match. | optional | string | n/a | | no | | K00370 |
| kegg_name | The Kegg Orthology name for the best Kegg match. | optional | string | n/a | | no | | narG, narZ, nxrA |
| kegg_description | The Kegg Orthology Entry definition of corresponding Kegg ID.| optional | string | n/a | | no | | nitrate reductase / nitrite oxidoreductase, alpha subunit [EC:1.7.5.1 1.7.99.-] |
| kegg_pathway | The relevant Kegg Pathway names for the corresponding Kegg ID.| optional | string | n/a | separate multiple-values with '\|\|' | yes | | Nitrogen metabolism \|\| Two-component system |
| pfams_id | The PFams identifier.| optional | string | n/a | | yes | | PF00886 |
| pfams_name | The PFams name as it rrelated to the associated PFams identifier. | optional | string | n/a | separate multiple-values with '\|\|' | yes | | Ribosomal protein S16 |
| uniprot_id | The Uniprot identifier.| optional | string | n/a | separate multiple-values with '\|\|' | yes | | A8G695 |
| enzyme_comm_id | The Enzyme Commission identifer. | optional | string | n/a | separate multiple-values with '\|\|' | yes | | |
| other_identified_proteins | Other protein IDs from the FASTA file| optional | string | n/a | separate multiple-values with '\|\|' | yes | A protein identifier in the FASTA file | |

[back to top](#)

## Peptide Spectral Count Field Names, Descriptions, Units ##
(_[as CSV](https://github.com/oceanproteinportal/data-file-templates/raw/master/tabular/TEMPLATE_Peptide_README.csv)_)

| peptide spectral count fields | Definition | required, recommended or optional | data type | units | format | multi-valued data cell? | relationships between files | example |
|-------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------|-----------|-----------------|------------|-------------------------|---------------------------------------------------------|-----------------------------------------|
| sample_id | Identifies the sample associated with this annotation| required | string | n/a | | no | | st6_200m_CID|
| cruise_id | Identifies the cruise related to the protein from which this peptide was derived | required | string | n/a | | no | | KM1128|
| station_id| Identifies the station related to the protein from which this peptide was derived | required | string | n/a | | no | | 6 |
| latitude_dd | The latitude at the station in decimal degrees (-90 to 90) related to the protein from which this peptide was derived| required| float | decimal degrees | | no | | 17|
| longitude_dd| The longitude at the station in decimal degrees (-180 to 180)related to the protein from which this peptide was derived| required| float | decimal degrees | | no | | -154.4|
| depth_m | The depth in meters at which the sample as taken related to the protein from which this peptide was derived| required| float | meters| | no | | 200 |
| date_y-m-d | The local date of sample collection related to the protein from which this peptide was derived | required| string | n/a | yyyy-mm-dd | no | | 2011-10-17|
| time_h-m-s | The local time of sample collection related to the protein from which this peptide was derived. Hour and minutes should be provided. Seconds optional. | recommended | string | n/a | hh:mm[:ss] | no | | 23:30 |
| minimum_filter_size_microns | Minimum size of the collection filter in microns related to the protein from which this peptide was derived| required| float | microns | | no | | 0.2 |
| maximum_filter_size_microns | Maximum size of the collection filter in microns related to the protein from which this peptide was derived| required| float | microns | | no | | 3 |
| peptide_sequence | The genomic sequence | required | string | n/a | | no | | |
| peptide_start_index | | required | integer | n/a | | no | | |
| peptide_stop_index | | required | integer | n/a | | no | | |
| protein_molecular_weight_kDa | The molecular weight in kilo-Daltons of the related protein| optional | float | kDa | | no | | |
| protein_id | | required | string | n/a | | no | The protein identifier from the protein spectral counts | |
| spectral_count_sum | | recommended | integer | n/a | | no | | |
| other_protein_ids | | optional | string | n/a | | no | A protein identifier from the protein spectral counts | |
| best_protein_id_probability | A probability (0-1) identifying the quality of the protein identification | optional | float | n/a | | no | | |
| best_sequest_DCn_score | | optional | | n/a | | no | | |
| best_sequest_Xcorr_score | | optional | | n/a | | no | | |
| plus2H_spectra_count | | optional | integer | n/a | | no | | |
| plus3H_spectra_count | | optional | integer | n/a | | no | | |
| plus4H_spectra_count | | optional | integer | n/a | | no | | |
| median_retention_time | | optional | | n/a | | no | | |
| total_precursor_intensity | | optional | | n/a | | no | | |
| TIC | Total Ion Chromatogram | optional | | n/a | | no | | |
| absolute_units_fmol-L | | optional | float | fmol/L | | no | | | 
  
[back to top](#)
