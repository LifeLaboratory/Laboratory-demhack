-- Table: public.person

-- DROP TABLE public.person;

CREATE TABLE public.person
(
  id_person integer NOT NULL DEFAULT nextval('person_id_person_seq'::regclass),
  name text,
  description text,
  pic text,
  health double precision,
  food double precision,
  leisure double precision,
  communication double precision,
  value integer,
  CONSTRAINT person_pk PRIMARY KEY (id_person)
)
WITH (
  OIDS=FALSE
);
ALTER TABLE public.person
  OWNER TO postgres;

-- Index: public.person_id_person_uindex

-- DROP INDEX public.person_id_person_uindex;

CREATE UNIQUE INDEX person_id_person_uindex
  ON public.person
  USING btree
  (id_person);

