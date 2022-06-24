from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
import sqlalchemy

db = SQLAlchemy()


class Study(db.Model):
    __tablename__ = 't_study_prof'
    __table_args__ = (
        db.PrimaryKeyConstraint('study_sk', name='t_study_prof_pk'),
        db.UniqueConstraint('unq_study_id', name='t_study_prof_ak'),
        {
            'comment': 'Housekeeping table for all studies.',
            'schema': 'GPDIP_DATATAGGING_DEV'
        }
    )

    study_sk = db.Column(db.Integer, primary_key=True, autoincrement=True,index = True,
                         comment='Sequence number assigned the record for the study')
    unq_study_id = db.Column(db.String(10), nullable=False, comment='Unique identifier assigned to the study')
    data_src_entity = db.Column(db.String(60), nullable=False, comment='Source entity for the study')
    protocol_id = db.Column(db.String(10), nullable=True, comment='Protocol identifier assigned to the study')
    study_name = db.Column(db.String(60), nullable=True, comment='Name assigned to the study')
    status_cd = db.Column(db.String(30), nullable=True, comment='Status of the study')
    study_start_ts = db.Column(db.DateTime(timezone=True), nullable=False, comment='Start date of the study')
    study_end_ts = db.Column(db.DateTime(timezone=True), nullable=False, comment='End date of the study')
    therapeutic_area = db.Column(db.String(60), nullable=True, comment='Therapeutic Area of the study')
    compound_asset = db.Column(db.String(50), nullable=True, comment='Compound asset of the study')
    global_clinical_lead = db.Column(db.String(100), nullable=True, comment='Global clinical lead of the study')
    study_desc = db.Column(db.String(300), nullable=True, comment='Verbiage of the study')
    approved_secondary_usage = db.Column(db.String(50), nullable=False, comment='')
    approved_sharing_internally_flag = db.Column(db.String(50), nullable=False, comment='')
    approved_sharing_externally_flag = db.Column(db.String(50), nullable=False, comment='')
    use_restriction_flag = db.Column(db.String(50), nullable=False, comment='')
    regulatory_retention_requirement_flag = db.Column(db.String(50), nullable=False, comment='')
    last_upd_ts = db.Column(db.DateTime(timezone=True), nullable=False, server_default=sqlalchemy.sql.func.now(),
                            onupdate=sqlalchemy.sql.func.now(), comment='Datetime when the record was updated')
    site = relationship('Site', back_populates='study')
    subject = relationship('Subject', back_populates='study')
    dataset = relationship('Dataset', back_populates='study')
    #consent = relationship('Consent', back_populates='study')
    #dataset_type = relationship('Dataset_Type', back_populates='study')


class Site(db.Model):
    __tablename__ = 't_site_prof'
    __table_args__ = (
        # db.PrimaryKeyConstraint('site_sk', name='t_site_prof_pk'),
        db.UniqueConstraint('unq_site_id', name='t_site_prof_ak'),
        {
            'comment': 'Housekeeping table for all sites',
            'schema': 'GPDIP_DATATAGGING_DEV'
        }
    )

    site_sk = db.Column(db.Integer, primary_key=True, autoincrement=True,index = True,
                        comment='Sequence number assigned the record for the site')
    unq_site_id = db.Column(db.String(40), nullable=False, comment='Unique identifier assigned to the site')
    site_id = db.Column(db.String(10), nullable=False, comment='site id')
    study_fk = db.Column(db.Integer, db.ForeignKey('GPDIP_DATATAGGING_DEV.t_study_prof.study_sk',
                                                   name='t_site_prof_to_t_study_prof_fk', onupdate="CASCADE",
                                                   ondelete="RESTRICT"), nullable=False,
                         comment='Sequence number assigned the record for the study')
    origin_ctry_cd = db.Column(db.String(30), nullable=True, comment='Origin country of the site')
    dest_ctry_cd = db.Column(db.String(30), nullable=True, comment='Destination country of the site')
    approved_secondary_usage = db.Column(db.String(50), nullable=False, comment='')
    approved_sharing_internally_flag = db.Column(db.String(50), nullable=False, comment='')
    approved_sharing_externally_flag = db.Column(db.String(50), nullable=False, comment='')
    use_restriction_flag = db.Column(db.String(50), nullable=False, comment='')
    regulatory_retention_requirement_flag = db.Column(db.String(50), nullable=False, comment='')
    no_of_sites = db.Column(db.Integer, nullable=True, comment='no of sites')
    last_upd_ts = db.Column(db.DateTime(timezone=True), nullable=False, server_default=sqlalchemy.sql.func.now(),
                            onupdate=sqlalchemy.sql.func.now(), comment='Datetime when the record was updated')
    study = relationship('Study', back_populates='site')
    subject = relationship('Subject', back_populates='site')
    dataset = relationship('Dataset', back_populates='site')
    consent = relationship('Consent', back_populates='site')
    #dataset_type = relationship('Dataset_Type', back_populates='site')


class Subject(db.Model):
    __tablename__ = 't_subj_prof'
    __table_args__ = (
        db.PrimaryKeyConstraint('subj_sk', name='t_subj_prof_pk'),
        db.UniqueConstraint('unq_subj_id', name='t_subj_prof_ak'),
        {
            'comment': 'Housekeeping table for all subjects',
            'schema': 'GPDIP_DATATAGGING_DEV'
        }
    )

    subj_sk = db.Column(db.Integer, primary_key=True, autoincrement=True,index = True,
                        comment='Sequence number assigned the record for the subject')
    unq_subj_id = db.Column(db.String(60), nullable=False, comment='Unique identifier assigned to the subject')
    subj_id = db.Column(db.String(20), nullable=False, comment='subject id')
    study_fk = db.Column(db.Integer, db.ForeignKey('GPDIP_DATATAGGING_DEV.t_study_prof.study_sk',
                                                   name='t_subj_prof_to_t_study_prof_fk', onupdate="CASCADE",
                                                   ondelete="RESTRICT"), nullable=False,
                         comment='Sequence number assigned the record for the study')
    latest_site_fk = db.Column(db.Integer, db.ForeignKey('GPDIP_DATATAGGING_DEV.t_site_prof.site_sk',
                                                         name='t_subj_prof_to_t_site_prof_fk', onupdate="CASCADE",
                                                         ondelete="RESTRICT"), nullable=True,
                               comment='Sequence number assigned the record for the site')
    gender_cd = db.Column(db.String(2), nullable=True, comment='Gender of the subject')
    no_of_study_subj = db.Column(db.Integer, nullable=True, comment='no of study subject')
    no_of_subjects = db.Column(db.Integer, nullable=True, comment='no of subjects')
    ethnicity_cd = db.Column(db.String(100), nullable=True, comment='Ethnicity of the subject')
    race_cd = db.Column(db.String(50), nullable=True, comment='Race of the subject')
    age = db.Column(db.Integer, nullable=True, comment='Age of the subject')
    residency_ctry_cd = db.Column(db.String(5), nullable=True, comment='Residency country of the subject')
    last_upd_ts = db.Column(db.DateTime(timezone=True), nullable=False, server_default=sqlalchemy.sql.func.now(),
                            onupdate=sqlalchemy.sql.func.now(), comment='Datetime when the record was updated')
    study = relationship('Study', back_populates='subject')
    site = relationship('Site', back_populates='subject')
    dataset = relationship('Dataset', back_populates='subject')
    #consent = relationship('Consent', back_populates='subject')
    #dataset_type = relationship('Dataset_Type', back_populates='subject')

class Dataset_Type(db.Model):
    __tablename__ = 't_dataset_type_prof'
    __table_args__ = (
        db.PrimaryKeyConstraint('dataset_type_sk', name='t_dataset_type_prof_pk'),
        db.UniqueConstraint('dataset_type_name', name='t_dataset_type_prof_ak'),
        {
            'comment': 'Housekeeping table for all subjects',
            'schema': 'GPDIP_DATATAGGING_DEV'
        }
    )

    dataset_type_sk = db.Column(db.Integer, primary_key=True, autoincrement=True,index = True,
                                comment='Sequence number assigned the record for the dataset type')
    dataset_type_name = db.Column(db.String(30), nullable=False,
                                  comment='Unique identifier assigned to the dataset_type')
    dataset_type = db.Column(db.String(30), nullable=True, comment='dataset type')
    dataset_file_type = db.Column(db.String(20), nullable=True, comment='dataset file type')
    last_upd_ts = db.Column(db.DateTime(timezone=True), nullable=False, server_default=sqlalchemy.sql.func.now(),
                            onupdate=sqlalchemy.sql.func.now(), comment='Datetime when the record was updated')
    dataset = relationship('Dataset', back_populates='dataset_type')
    #consent = relationship('Consent', back_populates='dataset_type')
    #study = relationship('Study', back_populates='dataset_type')
    #site = relationship('Site', back_populates='dataset_type')
    #subject = relationship('Subject', back_populates='dataset_type')

class Dataset(db.Model):
    __tablename__ = 't_dataset_prof'
    __table_args__ = (
        db.PrimaryKeyConstraint('dataset_sk', name='t_dataset_prof_pk'),
        db.UniqueConstraint('unq_dataset_id', name='t_dataset_prof_ak'),
        {
            'comment': 'Housekeeping table for all subjects',
            'schema': 'GPDIP_DATATAGGING_DEV'
        }
    )

    dataset_sk = db.Column(db.Integer, primary_key=True, autoincrement=True,index = True,
                           comment='Sequence number assigned the record for the dataset type')
    unq_dataset_id = db.Column(db.String(500), nullable=False, comment='Unique identifier assigned to the dataset_type')
    dataset_type_fk = db.Column(db.Integer, db.ForeignKey('GPDIP_DATATAGGING_DEV.t_dataset_type_prof.dataset_type_sk',
                                                          name='t_dataset_type_prof_to_t_dataset_prof_fk',
                                                          onupdate="CASCADE", ondelete="RESTRICT"), nullable=False,
                                comment='Sequence number assigned the record for the dataset type')
    study_fk = db.Column(db.Integer, db.ForeignKey('GPDIP_DATATAGGING_DEV.t_study_prof.study_sk',
                                                   name='t_dataset_type_prof_to_t_study_prof_fk', onupdate="CASCADE",
                                                   ondelete="RESTRICT"), nullable=False,
                         comment='Sequence number assigned the record for the study')
    subj_fk = db.Column(db.Integer, db.ForeignKey('GPDIP_DATATAGGING_DEV.t_subj_prof.subj_sk',
                                                  name='t_dataset_type_prof_to_t_subj_prof_fk', onupdate="CASCADE",
                                                  ondelete="RESTRICT"), nullable=False,
                        comment='Sequence number assigned the record for the subject')
    site_fk = db.Column(db.Integer, db.ForeignKey('GPDIP_DATATAGGING_DEV.t_site_prof.site_sk',
                                                  name='t_dataset_type_prof_to_t_site_prof_fk', onupdate="CASCADE",
                                                  ondelete="RESTRICT"), nullable=False,
                        comment='Sequence number assigned the record for the site')
    file_path = db.Column(db.String(150), nullable=True, comment='')
    file_name = db.Column(db.String(120), nullable=True, comment='')
    file_type = db.Column(db.String(10), nullable=True, comment='')
    data_zone = db.Column(db.String(20), nullable=True, comment='')
    degree_of_anonymization = db.Column(db.String(20), nullable=True, comment='')
    acquisition_date = db.Column(db.DateTime(timezone=True), nullable=True, comment='')
    acquisition_timepoint_name = db.Column(db.String(100), nullable=True, comment='')
    approved_secondary_usage = db.Column(db.String(50), nullable=False, comment='')
    approved_sharing_internally_flag = db.Column(db.String(50), nullable=False, comment='')
    approved_sharing_externally_flag = db.Column(db.String(50), nullable=False, comment='')
    use_restriction_flag = db.Column(db.String(50), nullable=False, comment='')
    regulatory_retention_requirement_flag = db.Column(db.String(50), nullable=False, comment='')
    last_upd_ts = db.Column(db.DateTime(timezone=True), nullable=False, server_default=sqlalchemy.sql.func.now(),
                            onupdate=sqlalchemy.sql.func.now(), comment='Datetime when the record was updated')
    study = relationship('Study', back_populates='dataset')
    site = relationship('Site', back_populates='dataset')
    subject = relationship('Subject', back_populates='dataset')
    dataset_type = relationship('Dataset_Type', back_populates='dataset')
    #consent = relationship('Consent', back_populates='dataset')

class Consent(db.Model):
    __tablename__ = 't_consent_prof'
    __table_args__ = (
        db.PrimaryKeyConstraint('site_consent_sk', name='t_consent_prof_pk'),
        db.UniqueConstraint('unq_consent_id', name='t_consent_prof_ak'),
        {
            'comment': 'Housekeeping table for all subjects',
            'schema': 'GPDIP_DATATAGGING_DEV'
        }
    )

    site_consent_sk = db.Column(db.Integer, primary_key=True, autoincrement=True,index = True,
                                comment='Sequence number assigned the record for the consent')
    unq_consent_id = db.Column(db.String(200), nullable=False, comment='Unique identifier assigned to the conesent')
    document_name = db.Column(db.String(100), nullable=False, comment='document name')
    site_fk = db.Column(db.Integer, db.ForeignKey('GPDIP_DATATAGGING_DEV.t_site_prof.site_sk',
                                                  name='t_consent_prof_to_t_site_prof_fk', onupdate="CASCADE",
                                                  ondelete="RESTRICT"), nullable=False,
                        comment='Sequence number assigned the record for the site')
    privacy_language_constructs = db.Column(db.String(10), nullable=False, comment='')
    hipaa_authorization = db.Column(db.String(50), nullable=False, comment='')
    data_users_sponsors = db.Column(db.String(50), nullable=False, comment='')
    data_users_people_organizations = db.Column(db.String(50), nullable=False, comment='')
    data_users_any_organization = db.Column(db.String(50), nullable=False, comment='')
    data_users_researchers = db.Column(db.String(50), nullable=False, comment='')
    data_users_irb_iec = db.Column(db.String(50), nullable=False, comment='')
    data_users_government = db.Column(db.String(50), nullable=False, comment='')
    data_users_primary_use_protocol = db.Column(db.String(50), nullable=False, comment='')
    data_users_use_outside_protocol = db.Column(db.String(50), nullable=False, comment='')
    degree_of_anonymization_in_icd = db.Column(db.String(150), nullable=True, comment='')
    consent_type_main_icd = db.Column(db.String(50), nullable=False, comment='')
    consent_type_additional_research = db.Column(db.String(100), nullable=True, comment='')
    consent_type_optional_procedure = db.Column(db.String(100), nullable=True, comment='')
    consent_type_banked_biospecimen = db.Column(db.String(100), nullable=False, comment='')
    retention_period_clinical_information = db.Column(db.String(50), nullable=True, comment='')
    retention_period_banked_biospecimen = db.Column(db.String(50), nullable=True, comment='')
    retention_period_tissue_samples = db.Column(db.String(50), nullable=True, comment='')
    last_upd_ts = db.Column(db.DateTime(timezone=True), nullable=False, server_default=sqlalchemy.sql.func.now(),
                            onupdate=sqlalchemy.sql.func.now(), comment='Datetime when the record was updated')
    #study = relationship('Study', back_populates='consent')
    site = relationship('Site', back_populates='consent')
    #subject = relationship('Subject', back_populates='consent')
    #dataset_type = relationship('Dataset_Type', back_populates='consent')
    #dataset = relationship('Dataset', back_populates='consent')


class Driver(db.Model):
    __tablename__ = 't_driver_table'
    __table_args__ = (
        db.PrimaryKeyConstraint('run_id', name='t_driver_table_pk'),
        {
            'comment': 'Housekeeping table for checking the status ',
            'schema': 'GPDIP_DATATAGGING_DEV'
         }
    )

    run_id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False, comment='')
    table_name = db.Column(db.String(20), nullable=True, comment='')
    status = db.Column(db.String(20), nullable=True, comment='')
    load_date = db.Column(db.DateTime(timezone=True), nullable=True, comment='')


class Config(db.Model):
    __tablename__ = 't_config_fl'
    __table_args__ = (
        db.PrimaryKeyConstraint('id', name='t_config_fl_pk'),
        {
             'comment': 'Housekeeping table for all flag values ',
              'schema': 'GPDIP_DATATAGGING_DEV'
        }
    )

    id = db.Column(db.String(10), primary_key=True,nullable=False, comment='')
    type = db.Column(db.String(50), nullable=False, comment='')
    approved_secondary_usage = db.Column(db.String(50), nullable=True, comment='')
    approved_sharing_internally_flag = db.Column(db.String(50), nullable=True, comment='')
    approved_sharing_externally_flag = db.Column(db.String(50), nullable=True, comment='')
    use_restriction_flag = db.Column(db.String(50), nullable=True, comment='')
    regulatory_retention_requirement_flag = db.Column(db.String(50), nullable=True, comment='')



    #consent = relationship('Consent', back_populates='study')
    #dataset_type = relationship('Dataset_Type', back_populates='study')


class study_like_view(db.Model):
    __tablename__ = 't_study_like_view'
    __table_args__ = (

        {
            'comment': 'Housekeeping table for all studies.',
            'schema': 'GPDIP_DATATAGGING_DEV'
        }
    )

    GPDIP_DATATAGGING_DEV_t_study_prof_study_sk = db.Column(db.Integer,  index=True,
                                                            comment='Sequence number assigned the record for the study')
    GPDIP_DATATAGGING_DEV_t_study_prof_unq_study_id = db.Column(db.String(10), nullable=False,
                                                                comment='Unique identifier assigned to the study')
    GPDIP_DATATAGGING_DEV_t_study_prof_data_src_entity = db.Column(db.String(60), nullable=False,
                                                                   comment='Source entity for the study')
    GPDIP_DATATAGGING_DEV_t_study_prof_protocol_id = db.Column(db.String(10), nullable=True,
                                                               comment='Protocol identifier assigned to the study')
    GPDIP_DATATAGGING_DEV_t_study_prof_study_name = db.Column(db.String(60), nullable=True,
                                                              comment='Name assigned to the study')
    GPDIP_DATATAGGING_DEV_t_study_prof_status_cd = db.Column(db.String(30), nullable=True,
                                                             comment='Status of the study')
    GPDIP_DATATAGGING_DEV_t_study_prof_study_start_ts = db.Column(db.DateTime(timezone=True), nullable=False,
                                                                  comment='Start date of the study')
    GPDIP_DATATAGGING_DEV_t_study_prof_study_end_ts = db.Column(db.DateTime(timezone=True), nullable=False,
                                                                comment='End date of the study')
    GPDIP_DATATAGGING_DEV_t_study_prof_therapeutic_area = db.Column(db.String(60), nullable=True,
                                                                    comment='Therapeutic Area of the study')
    GPDIP_DATATAGGING_DEV_t_study_prof_compound_asset = db.Column(db.String(50), nullable=True,
                                                                  comment='Compound asset of the study')
    GPDIP_DATATAGGING_DEV_t_study_prof_global_clinical_lead = db.Column(db.String(100), nullable=True,
                                                                        comment='Global clinical lead of the study')
    GPDIP_DATATAGGING_DEV_t_study_prof_study_desc = db.Column(db.String(300), nullable=True,
                                                              comment='Verbiage of the study')
    GPDIP_DATATAGGING_DEV_t_study_prof_approved_secondary_usage = db.Column(db.String(50), nullable=False, comment='')
    GPDIP_DATATAGGING_DEV_t_study_prof_approved_sharing_internally_flag = db.Column(db.String(50), nullable=False,
                                                                                    comment='')
    GPDIP_DATATAGGING_DEV_t_study_prof_approved_sharing_externally_flag = db.Column(db.String(50), nullable=False,
                                                                                    comment='')
    GPDIP_DATATAGGING_DEV_t_study_prof_use_restriction_flag = db.Column(db.String(50), nullable=False, comment='')
    GPDIP_DATATAGGING_DEV_t_study_prof_regulatory_retention_requirement_flag = db.Column(db.String(50), nullable=False,
                                                                                         comment='')
    
    GPDIP_DATATAGGING_DEV_t_site_prof_site_sk = db.Column(db.Integer,index = True,
                        comment='Sequence number assigned the record for the site')
    GPDIP_DATATAGGING_DEV_t_site_prof_unq_site_id = db.Column(db.String(40), nullable=False, comment='Unique identifier assigned to the site')
    GPDIP_DATATAGGING_DEV_t_site_prof_site_id = db.Column(db.String(10), nullable=False, comment='site id')
    GPDIP_DATATAGGING_DEV_t_site_prof_study_fk = db.Column(db.Integer, db.ForeignKey('GPDIP_DATATAGGING_DEV.t_study_prof.study_sk',
                                                   name='t_site_prof_to_t_study_prof_fk', onupdate="CASCADE",
                                                   ondelete="RESTRICT"), nullable=False,
                         comment='Sequence number assigned the record for the study')
    GPDIP_DATATAGGING_DEV_t_site_prof_origin_ctry_cd = db.Column(db.String(30), nullable=True, comment='Origin country of the site')
    GPDIP_DATATAGGING_DEV_t_site_prof_dest_ctry_cd = db.Column(db.String(30), nullable=True, comment='Destination country of the site')
    GPDIP_DATATAGGING_DEV_t_site_prof_approved_secondary_usage = db.Column(db.String(50), nullable=False, comment='')
    GPDIP_DATATAGGING_DEV_t_site_prof_approved_sharing_internally_flag = db.Column(db.String(50), nullable=False, comment='')
    GPDIP_DATATAGGING_DEV_t_site_prof_approved_sharing_externally_flag = db.Column(db.String(50), nullable=False, comment='')
    GPDIP_DATATAGGING_DEV_t_site_prof_use_restriction_flag = db.Column(db.String(50), nullable=False, comment='')
    GPDIP_DATATAGGING_DEV_t_site_prof_regulatory_retention_requirement_flag = db.Column(db.String(50), nullable=False, comment='')
    GPDIP_DATATAGGING_DEV_t_site_prof_no_of_sites = db.Column(db.Integer, nullable=True, comment='no of sites')
    GPDIP_DATATAGGING_DEV_t_subj_prof_subj_sk = db.Column(db.Integer,index = True,
                        comment='Sequence number assigned the record for the subject')
    GPDIP_DATATAGGING_DEV_t_subj_prof_unq_subj_id = db.Column(db.String(60), nullable=False, comment='Unique identifier assigned to the subject')
    GPDIP_DATATAGGING_DEV_t_subj_prof_subj_id = db.Column(db.String(20), nullable=False, comment='subject id')
    GPDIP_DATATAGGING_DEV_t_subj_prof_study_fk = db.Column(db.Integer, db.ForeignKey('GPDIP_DATATAGGING_DEV.t_study_prof.study_sk',
                                                   name='t_subj_prof_to_t_study_prof_fk', onupdate="CASCADE",
                                                   ondelete="RESTRICT"), nullable=False,
                         comment='Sequence number assigned the record for the study')
    GPDIP_DATATAGGING_DEV_t_subj_prof_latest_site_fk = db.Column(db.Integer, db.ForeignKey('GPDIP_DATATAGGING_DEV.t_site_prof.site_sk',
                                                         name='t_subj_prof_to_t_site_prof_fk', onupdate="CASCADE",
                                                         ondelete="RESTRICT"), nullable=True,
                               comment='Sequence number assigned the record for the site')
    GPDIP_DATATAGGING_DEV_t_subj_prof_gender_cd = db.Column(db.String(2), nullable=True, comment='Gender of the subject')
    GPDIP_DATATAGGING_DEV_t_subj_prof_no_of_study_subj = db.Column(db.Integer, nullable=True, comment='no of study subject')
    GPDIP_DATATAGGING_DEV_t_subj_prof_no_of_subjects = db.Column(db.Integer, nullable=True, comment='no of subjects')
    GPDIP_DATATAGGING_DEV_t_subj_prof_ethnicity_cd = db.Column(db.String(100), nullable=True, comment='Ethnicity of the subject')
    GPDIP_DATATAGGING_DEV_t_subj_prof_race_cd = db.Column(db.String(50), nullable=True, comment='Race of the subject')
    GPDIP_DATATAGGING_DEV_t_subj_prof_age = db.Column(db.Integer, nullable=True, comment='Age of the subject')
    GPDIP_DATATAGGING_DEV_t_subj_prof_residency_ctry_cd = db.Column(db.String(5), nullable=True, comment='Residency country of the subject')
    GPDIP_DATATAGGING_DEV_t_dataset_prof_dataset_sk = db.Column(db.Integer,index = True,
                           comment='Sequence number assigned the record for the dataset type')
    GPDIP_DATATAGGING_DEV_t_dataset_prof_unq_dataset_id = db.Column(db.String(500), nullable=False, comment='Unique identifier assigned to the dataset_type')
    GPDIP_DATATAGGING_DEV_t_dataset_prof_dataset_type_fk = db.Column(db.Integer, db.ForeignKey('GPDIP_DATATAGGING_DEV.t_dataset_type_prof.dataset_type_sk',
                                                          name='t_dataset_type_prof_to_t_dataset_prof_fk',
                                                          onupdate="CASCADE", ondelete="RESTRICT"), nullable=False,
                                comment='Sequence number assigned the record for the dataset type')
    GPDIP_DATATAGGING_DEV_t_dataset_prof_study_fk = db.Column(db.Integer, db.ForeignKey('GPDIP_DATATAGGING_DEV.t_study_prof.study_sk',
                                                   name='t_dataset_type_prof_to_t_study_prof_fk', onupdate="CASCADE",
                                                   ondelete="RESTRICT"), nullable=False,
                         comment='Sequence number assigned the record for the study')
    GPDIP_DATATAGGING_DEV_t_dataset_prof_subj_fk = db.Column(db.Integer, db.ForeignKey('GPDIP_DATATAGGING_DEV.t_subj_prof.subj_sk',
                                                  name='t_dataset_type_prof_to_t_subj_prof_fk', onupdate="CASCADE",
                                                  ondelete="RESTRICT"), nullable=False,
                        comment='Sequence number assigned the record for the subject')
    GPDIP_DATATAGGING_DEV_t_dataset_prof_site_fk = db.Column(db.Integer, db.ForeignKey('GPDIP_DATATAGGING_DEV.t_site_prof.site_sk',
                                                  name='t_dataset_type_prof_to_t_site_prof_fk', onupdate="CASCADE",
                                                  ondelete="RESTRICT"), nullable=False,
                        comment='Sequence number assigned the record for the site')
    GPDIP_DATATAGGING_DEV_t_dataset_prof_file_path = db.Column(db.String(150), nullable=True, comment='')
    GPDIP_DATATAGGING_DEV_t_dataset_prof_file_name = db.Column(db.String(120), nullable=True, comment='')
    GPDIP_DATATAGGING_DEV_t_dataset_prof_file_type = db.Column(db.String(10), nullable=True, comment='')
    GPDIP_DATATAGGING_DEV_t_dataset_prof_data_zone = db.Column(db.String(20), nullable=True, comment='')
    GPDIP_DATATAGGING_DEV_t_dataset_prof_degree_of_anonymization = db.Column(db.String(20), nullable=True, comment='')
    GPDIP_DATATAGGING_DEV_t_dataset_prof_acquisition_date = db.Column(db.DateTime(timezone=True), nullable=True, comment='')
    GPDIP_DATATAGGING_DEV_t_dataset_prof_acquisition_timepoint_name = db.Column(db.String(100), nullable=True, comment='')
    GPDIP_DATATAGGING_DEV_t_dataset_prof_approved_secondary_usage = db.Column(db.String(50), nullable=False, comment='')
    GPDIP_DATATAGGING_DEV_t_dataset_prof_approved_sharing_internally_flag = db.Column(db.String(50), nullable=False, comment='')
    GPDIP_DATATAGGING_DEV_t_dataset_prof_approved_sharing_externally_flag = db.Column(db.String(50), nullable=False, comment='')
    GPDIP_DATATAGGING_DEV_t_dataset_prof_use_restriction_flag = db.Column(db.String(50), nullable=False, comment='')
    GPDIP_DATATAGGING_DEV_t_dataset_prof_regulatory_retention_requirement_flag = db.Column(db.String(50), nullable=False, comment='')
    GPDIP_DATATAGGING_DEV_t_dataset_type_prof_dataset_type_sk = db.Column(db.Integer,index = True,
                                comment='Sequence number assigned the record for the dataset type')
    GPDIP_DATATAGGING_DEV_t_dataset_type_prof_dataset_type_name = db.Column(db.String(30), nullable=False,
                                  comment='Unique identifier assigned to the dataset_type')
    GPDIP_DATATAGGING_DEV_t_dataset_type_prof_dataset_type = db.Column(db.String(30), nullable=True, comment='dataset type')
    GPDIP_DATATAGGING_DEV_t_dataset_type_prof_dataset_file_type = db.Column(db.String(20), nullable=True, comment='dataset file type')