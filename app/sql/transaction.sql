-- Table: public.transaction

-- DROP TABLE public.transaction;

CREATE TABLE public.transaction
(
  id_game integer,
  worked boolean,
  call boolean,
  id_transaction integer NOT NULL DEFAULT nextval('transaction_id_transaction_seq'::regclass),
  id_user integer,
  covid boolean,
  CONSTRAINT transaction_pk PRIMARY KEY (id_transaction)
)
WITH (
  OIDS=FALSE
);
ALTER TABLE public.transaction
  OWNER TO postgres;

-- Index: public.transaction_id_transaction_uindex

-- DROP INDEX public.transaction_id_transaction_uindex;

CREATE UNIQUE INDEX transaction_id_transaction_uindex
  ON public.transaction
  USING btree
  (id_transaction);

