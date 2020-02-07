# Creating an Ocean Protein Portal Data Submission #

Data files and metadata should be submitted to the [Biological and Chemical Oceanography Data Management Office (BCO-DMO)](https://www.bco-dmo.org/).  Your data will be served from a Dataset Landing Page at BCO-DMO in addition to being imported into the Ocean Porotein Portal.

## Steps ##

### Format the data ###

Format your data according to the following templates.

Column names as a csv file:
* Protein Spectral Counts [[template](tabular/TEMPLATE_Protein-Spectral-Counts.csv)] _(csv)_
* FASTA of Protein Identifications
* Peptide Spectral Counts [[template](tabular/TEMPLATE_Peptide-Spectral-Counts.csv)] _(csv)_

Column descriptions, units, types, and requirements:
* [Protein Spectral Counts](#protein-spectral-counts) 
* Protein FASTA file
* [Peptide Spectral Counts](#peptide-spectral-counts)

Formatting instructions:
* Include all data columns labeled as "required" in your data.  
* Use the OPP templates column names in your data files.  
* Protein identifiers used in your FASTA file should match the identifiers in your spectral count data.
* Ensure that your data are processed, QA/QC’ed and research ready.  
* Check that your data are compliant with the types defined in the template (e.g. best_protein_id_probability is a float so shouldn’t include the % symbol).
* You can include additional columns not defined in the template.

### Fill out a metadata form ###

Download a copy of the BCO-DMO [DATASET.rtf](https://www.bco-dmo.org/files/bcodmo/DATASET.rtf) metadata form.

The form includes a section to document your **Parameter names, descriptions, units.**  You can download a copy of the template column names, descriptions and units csv files and modify them as needed so they correctly describe your data. 
* [Protein Spectral Counts: names, descriptions, units](TEMPLATE_README.csv#L1) (csv)
* [Peptide Spectral Counts: names, descriptions, units](TEMPLATE_README.csv#L27) (csv)

You can include these column descriptions directly in your DATASET.rtf metadata form, or include them as separate csv or Excel files in your submission.

Make sure to include in your column descriptions:
* The time zone of the date and time columns.
* Include any missing data identifiers used in your data (e.g. NA, nd, NaN, -999)
* For any cell that can store multiple values (e.g. other_protein_ids), please notify us of the string which identifies the delimiter between each value.

More guidance about preparing files for submission to BCO-DMO can be found on the [How To](https://www.bco-dmo.org/how-get-started) page.

### Submit your data ###

* Email your data files and a completed copy of the DATASET.rtf (metadata form) to info@bco-dmo.org.
* In your email, indicate that you would like the dataset included in the Ocean Protein Portal.

## What happens after I submit data?  ##

A data manager will:
* Confirm receipt of your dataset.  
* Create a public dataset landing page at BCO-DMO with the metadata you included in your DATASET.rtf metadata form.  
* Ask questions during the data serving process, and get back to you for your final review of the data and metadata before it is imported into OPP. 
* Publish your final, validated dataset on the BCO-DMO website.
* Mint a Digital Object Identifier (DOI) for your data.

If you have any questions about submitting data please contact **Contact Us @ [contact@oceanproteinportal.org](mailto:contact@oceanproteinportal.org)** or [info@bco-dmo.org](info@bco-dmo.org),

## Protein Spectral Counts ##
(_[view as CSV](TEMPLATE_README.csv#L1)_)

| protein spectral count fields | Definition                                                                                                                                             | required, recommended or optional | data type | units           | format     | multi-valued data cell? | relationships between files                             | example                                 | 
|-------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------|-----------|-----------------|------------|-------------------------|---------------------------------------------------------|-----------------------------------------| 
| sample_id                     | Identifies the sample associated with this annotation                                                                                                  | required                          | string    | n/a             |            | no                      |                                                         | st6_200m_CID                            | 
| cruise_id                     | Identifies the cruise on which collection occurred                                                                                                     | required                          | string    | n/a             |            | no                      |                                                         | KM1128                                  | 
| station_id                    | Identifies the station for the location this sample was taken                                                                                          | required                          | string    | n/a             |            | no                      |                                                         | 6                                       | 
| latitude_dd                   | The latitude at the station in decimal degrees (-90 to 90)                                                                                             | required                          | float     | decimal degrees |            | no                      |                                                         | 17                                      | 
| longitude_dd                  | The longitude at the station in decimal degrees (-180 to 180)                                                                                          | required                          | float     | decimal degrees |            | no                      |                                                         | -154.4                                  | 
| depth_m                       | The depth in meters at which the sample as taken                                                                                                       | required                          | float     | meters          |            | no                      |                                                         | 200                                     | 
| date_y-m-d                    | The date of sample collection                                                                                                                          | required                          | string    | n/a             | yyyy-mm-dd | no                      |                                                         | 2011-10-17                              | 
| time_h-m-s                    | The local time of sample collection. Hour and minutes should be provided. Seconds optional                                                             | recommended                       | string    | n/a             | hh:mm[:ss] | no                      |                                                         | 23:30                                   | 
| minimum_filter_size_microns   | Minimum size of the collection filter in microns                                                                                                       | required                          | float     | microns         |            | no                      |                                                         | 0.2                                     | 
| maximum_filter_size_microns   | Maximum size of the collection filter in microns                                                                                                       | required                          | float     | microns         |            | no                      |                                                         | 3                                       | 
| protein_id                    | An identifier that uniquely identifies this protein within this dataset and the FASTA file.                                                            | required                          | string    | n/a             |            | no                      | The protein identifier in the FASTA file                | NODE_+1234.5678                         | 
| protein_name                  | A name identifying this protein                                                                                                                        | required                          | string    | n/a             |            | no                      |                                                         | short-chain dehydrogenase/reductase SDR | 
| spectral_count                | The spectral count                                                                                                                                     | required                          | integer   | n/a             |            | no                      |                                                         | 2                                       | 
| molecular_weight_kDa          | The molecular weight in kilo-Daltons of the sample                                                                                                     | optional                          | float     | kDa             |            | no                      |                                                         | 45239.7                                 | 
| ncbi_id                       | The NCBI identifier.                                                                                                                                   | optional                          | string    | n/a             |            | no                      |                                                         | 479434                                  | 
| ncbi_name                     | The name as it corresponds to the preceding NCBI identifier                                                                                            | optional                          | string    | n/a             |            | no                      |                                                         | Sphaerobacter thermophilus DSM 20745    | 
| kegg_id                       | The Kegg identifier.                                                                                                                                   | optional                          | string    | n/a             |            | yes                     |                                                         |                                         | 
| kegg_description              | The Kegg description as it correlates to the preceding Kegg identifier.                                                                                | optional                          | string    | n/a             |            | yes                     |                                                         |                                         | 
| kegg_pathway                  | The Kegg pathway as it correlates to the preceding Kegg identifier.                                                                                    | optional                          | string    | n/a             |            | yes                     |                                                         |                                         | 
| pfams_id                      | The PFams identifier.                                                                                                                                  | optional                          | string    | n/a             |            | yes                     |                                                         | PF00886                                 | 
| pfams_name                    | The PFams name as it correlates to the preceding PFams identifier.                                                                                     | optional                          | string    | n/a             |            | yes                     |                                                         | Ribosomal protein S16                   | 
| uniprot_id                    | The Uniprot identifier.                                                                                                                                | optional                          | string    | n/a             |            | yes                     |                                                         | A8G695                                  | 
| enzyme_comm_id                | The Enzyme Commission identifer.                                                                                                                       | optional                          | string    | n/a             |            | yes                     |                                                         |                                         | 
| other_identified_proteins     | Other protein IDs from the FASTA file                                                                                                                  | optional                          | string    | n/a             |            | yes                     | A protein identifier in the FASTA file                  |                                         | 

[back to top](#)

## Peptide Spectral Counts ##
(_[view as CSV](TEMPLATE_README.csv#L27)_)

| peptide spectral count fields | Definition                                                                                                                                             | required, recommended or optional | data type | units           | format     | multi-valued data cell? | relationships between files                             | example                                 | 
|-------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------|-----------|-----------------|------------|-------------------------|---------------------------------------------------------|-----------------------------------------| 
| sample_id                     | Identifies the sample associated with this annotation                                                                                                  | required                          | string    | n/a             |            | no                      |                                                         | st6_200m_CID                            | 
| cruise_id                     | Identifies the cruise related to the protein from which this peptide was derived                                                                       | required                          | string    | n/a             |            | no                      |                                                         | KM1128                                  | 
| station_id                    | Identifies the station related to the protein from which this peptide was derived                                                                      | required                          | string    | n/a             |            | no                      |                                                         | 6                                       | 
| latitude_dd                   | The latitude at the station in decimal degrees (-90 to 90) related to the protein from which this peptide was derived                                  | required                          | float     | decimal degrees |            | no                      |                                                         | 17                                      | 
| longitude_dd                  | The longitude at the station in decimal degrees (-180 to 180)  related to the protein from which this peptide was derived                              | required                          | float     | decimal degrees |            | no                      |                                                         | -154.4                                  | 
| depth_m                       | The depth in meters at which the sample as taken related to the protein from which this peptide was derived                                            | required                          | float     | meters          |            | no                      |                                                         | 200                                     | 
| date_y-m-d                    | The local date of sample collection related to the protein from which this peptide was derived                                                               | required                          | string    | n/a             | yyyy-mm-dd | no                      |                                                         | 2011-10-17                              | 
| time_h-m-s                    | The local time of sample collection related to the protein from which this peptide was derived. Hour and minutes should be provided. Seconds optional. | recommended                       | string    | n/a             | hh:mm[:ss] | no                      |                                                         | 23:30                                   | 
| minimum_filter_size_microns   | Minimum size of the collection filter in microns related to the protein from which this peptide was derived                                            | required                          | float     | microns         |            | no                      |                                                         | 0.2                                     | 
| maximum_filter_size_microns   | Maximum size of the collection filter in microns related to the protein from which this peptide was derived                                            | required                          | float     | microns         |            | no                      |                                                         | 3                                       | 
| peptide_sequence              | The genomic sequence                                                                                                                                   | required                          | string    | n/a             |            | no                      |                                                         |                                         | 
| peptide_start_index           |                                                                                                                                                        | required                          | integer   | n/a             |            | no                      |                                                         |                                         | 
| peptide_stop_index            |                                                                                                                                                        | required                          | integer   | n/a             |            | no                      |                                                         |                                         | 
| protein_molecular_weight_kDa  | The molecular weight in kilo-Daltons of the related protein                                                                                            | optional                          | float     | kDa             |            | no                      |                                                         |                                         | 
| protein_id                    |                                                                                                                                                        | required                          | string    | n/a             |            | no                      | The protein identifier from the protein spectral counts |                                         | 
| spectral_count_sum            |                                                                                                                                                        | recommended                       | integer   | n/a             |            | no                      |                                                         |                                         | 
| other_protein_ids             |                                                                                                                                                        | optional                          | string    | n/a             |            | no                      | A protein identifier from the protein spectral counts   |                                         | 
| best_protein_id_probability   | A percentage identifying the quality of the protein identification                                                                                     | optional                          | float     | n/a             |            | no                      |                                                         |                                         | 
| best_sequest_DCn_score        |                                                                                                                                                        | optional                          |           | n/a             |            | no                      |                                                         |                                         | 
| best_sequest_Xcorr_score      |                                                                                                                                                        | optional                          |           | n/a             |            | no                      |                                                         |                                         | 
| plus2H_spectra_count          |                                                                                                                                                        | optional                          | integer   | n/a             |            | no                      |                                                         |                                         | 
| plus3H_spectra_count          |                                                                                                                                                        | optional                          | integer   | n/a             |            | no                      |                                                         |                                         | 
| plus4H_spectra_count          |                                                                                                                                                        | optional                          | integer   | n/a             |            | no                      |                                                         |                                         | 
| median_retention_time         |                                                                                                                                                        | optional                          |           | n/a             |            | no                      |                                                         |                                         | 
| total_precursor_intensity     |                                                                                                                                                        | optional                          |           | n/a             |            | no                      |                                                         |                                         | 
| TIC                           | Total Ion Chromatogram                                                                                                                                 | optional                          |           | n/a             |            | no                      |                                                         |                                         | 
| absolute_units_fmol-L         |                                                                                                                                                        | optional                          | float     | fmol/L          |            | no                      |                                                         |                                         | 
  
[back to top](#)
  
