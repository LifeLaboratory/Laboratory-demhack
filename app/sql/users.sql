-- Table: public.users

-- DROP TABLE public.users;

CREATE TABLE public.users
(
  id_user integer NOT NULL DEFAULT nextval('user_id_user_seq'::regclass),
  login text,
  password text,
  pic text,
  CONSTRAINT user_pk PRIMARY KEY (id_user)
)
WITH (
  OIDS=FALSE
);
ALTER TABLE public.users
  OWNER TO postgres;

-- Index: public.user_id_user_uindex

-- DROP INDEX public.user_id_user_uindex;

CREATE UNIQUE INDEX user_id_user_uindex
  ON public.users
  USING btree
  (id_user);

-- Index: public.user_login_uindex

-- DROP INDEX public.user_login_uindex;

CREATE UNIQUE INDEX user_login_uindex
  ON public.users
  USING btree
  (login COLLATE pg_catalog."default");

