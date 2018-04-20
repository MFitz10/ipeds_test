CREATE TABLE "CIPFamily" (
            "CIPFamily" integer PRIMARY KEY,
            "Name" character varying,
            "Stem" boolean
);

CREATE TABLE "JobCIP" (
            "id" serial PRIMARY KEY,
            "JobCode" character varying REFERENCES "Jobs" ("JobCode"),
            "CIPFamily" integer REFERENCES "CIPFamily" ("CIPFamily")
);

--NOTE: mark stem CIPs manually
INSERT INTO "CIPFamily" (
            SELECT DISTINCT "IPEDSID_1",
                        REGEXP_REPLACE(REGEXP_REPLACE(INITCAP("IPEDS_Job_Family"), 
                                    ' And ', ' and '), '\.', ''), FALSE
            FROM "major_main"
            ORDER BY "IPEDSID_1"
);

INSERT INTO "JobCIP" ("JobCode", "CIPFamily") (
            SELECT DISTINCT "JobCode", "IPEDSID_2" AS "CIPFamily"
            FROM (
                        SELECT "IDs".*, "Major"
                        FROM "IDs"
                        LEFT JOIN "Majors"
                        ON "IDs"."MajorID" = "Majors"."MajorID"
            ) "USAJOBS"
            LEFT JOIN "major_main"
            ON "USAJOBS"."Major" = "major_main"."USAJOBS_ALL"
            ORDER BY "JobCode"
);
