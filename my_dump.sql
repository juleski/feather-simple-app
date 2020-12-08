--
-- PostgreSQL database dump
--

-- Dumped from database version 13.1
-- Dumped by pg_dump version 13.1

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Data for Name: providers; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.providers (id, name, price, billing_period, for_occupation, created) VALUES ('0953efc2-9f2b-4fc4-a4b0-5ed0a78334d1', 'Job Insurance', 30.5, 'per month', 'employed', '2020-12-06 10:45:43.734384');
INSERT INTO public.providers (id, name, price, billing_period, for_occupation, created) VALUES ('6da3bc0f-2d1d-4511-9ba4-61bfffdf76b4', 'Life Insurance', 29.5, 'per month', 'employed', '2020-12-06 10:45:43.739473');
INSERT INTO public.providers (id, name, price, billing_period, for_occupation, created) VALUES ('ecdd54f3-3419-44f1-8542-2df7353c7764', 'Life Insurance', 8.95, 'per month', 'employed', '2020-12-06 10:45:43.740869');
INSERT INTO public.providers (id, name, price, billing_period, for_occupation, created) VALUES ('6e43e53c-4e59-4872-8d00-a1b65679dccc', 'Personal Liability', 7.45, 'per month', 'employed', '2020-12-06 10:45:43.742267');
INSERT INTO public.providers (id, name, price, billing_period, for_occupation, created) VALUES ('cdd9c77f-217f-4e17-8a70-81e91ef8081c', 'Personal Liability', 19.35, 'per month', 'employed', '2020-12-06 10:45:43.74347');
INSERT INTO public.providers (id, name, price, billing_period, for_occupation, created) VALUES ('fe5841f0-63bd-4bd3-aa07-cb4d875a4952', 'Car', 17.95, 'per month', 'employed', '2020-12-06 10:45:43.744761');
INSERT INTO public.providers (id, name, price, billing_period, for_occupation, created) VALUES ('e36b5187-c073-4268-8c2c-5e04cd5f3ffe', 'Car', 17.95, 'per month', 'employed', '2020-12-06 10:45:43.746554');
INSERT INTO public.providers (id, name, price, billing_period, for_occupation, created) VALUES ('9210e796-4fe1-4907-8e4e-b089c35be4dd', 'Health (private)', 32.5, 'per month', 'employed', '2020-12-06 10:45:43.747941');
INSERT INTO public.providers (id, name, price, billing_period, for_occupation, created) VALUES ('7dc0969e-4377-437e-bbce-425a0b04e2bd', 'Health (private)', 32.5, 'per month', 'self_employed', '2020-12-06 10:45:43.749278');
INSERT INTO public.providers (id, name, price, billing_period, for_occupation, created) VALUES ('7029ffb5-f32c-4a91-9cb0-768eb47cba4a', 'Personal Liability', 31.42, 'per month', 'self_employed', '2020-12-06 10:45:43.75061');
INSERT INTO public.providers (id, name, price, billing_period, for_occupation, created) VALUES ('6d82a544-179d-4fe9-a2e5-9b6d6d25c008', 'Personal Liability', 9.45, 'per month', 'self_employed', '2020-12-06 10:45:43.751956');
INSERT INTO public.providers (id, name, price, billing_period, for_occupation, created) VALUES ('f553892b-cfa7-4bea-bd31-d15c8581d283', 'Personal Liability', 16.45, 'per month', 'self_employed', '2020-12-06 10:45:43.753247');
INSERT INTO public.providers (id, name, price, billing_period, for_occupation, created) VALUES ('fd110434-5d13-45d7-aa19-33f0f2b2af61', 'Car', 19.25, 'per month', 'self_employed', '2020-12-06 10:45:43.754501');
INSERT INTO public.providers (id, name, price, billing_period, for_occupation, created) VALUES ('96f6d24e-f6f9-47cd-a8a7-4bb1ad1c047e', 'Car', 32.5, 'per month', 'self_employed', '2020-12-06 10:45:43.755915');
INSERT INTO public.providers (id, name, price, billing_period, for_occupation, created) VALUES ('a5692065-6fa7-43ea-bfab-80306756f17c', 'Personal Liability', 28.5, 'per month', 'student', '2020-12-06 10:45:43.757307');
INSERT INTO public.providers (id, name, price, billing_period, for_occupation, created) VALUES ('c9c86fd2-472b-4ac9-ada2-30d6f655fdb7', 'Life insurance', 19.5, 'per month', 'student', '2020-12-06 10:45:43.758836');
INSERT INTO public.providers (id, name, price, billing_period, for_occupation, created) VALUES ('cd56d6c1-c48b-4df0-9da4-de8f3c92368c', 'Job insurance', 31.5, 'per month', 'student', '2020-12-06 10:45:43.760054');
INSERT INTO public.providers (id, name, price, billing_period, for_occupation, created) VALUES ('5369a098-ca1e-4443-9ae1-cdbecb537c69', 'Personal Liability', 19.5, 'per month', 'student', '2020-12-06 10:45:43.761348');
INSERT INTO public.providers (id, name, price, billing_period, for_occupation, created) VALUES ('ebf87aa6-4e2d-4dfa-9a69-8b5b6a9d9f54', 'Life insurance', 8.95, 'per month', 'student', '2020-12-06 10:45:43.762781');
INSERT INTO public.providers (id, name, price, billing_period, for_occupation, created) VALUES ('fb252561-fa6f-4ed4-9493-e210bd637b22', 'Health (private)', 7.45, 'per month', 'student', '2020-12-06 10:45:43.764235');


--
-- PostgreSQL database dump complete
--

