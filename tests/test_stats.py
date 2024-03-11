import pytest
import os
from flask_stats.APIclient import APIclient

token = os.environ["CLI_TOKEN"]
return_payload = {
    "hits": {
        "hits": [
            {
                "id": "sdnj1-bkr82",
                "created": "2024-03-04T17:22:55.876533+00:00",
                "updated": "2024-03-04T17:22:55.987176+00:00",
                "links": {
                    "self": "https://invenio-dev.hcommons-staging.org/api/records/sdnj1-bkr82",
                    "self_html": "https://invenio-dev.hcommons-staging.org/records/sdnj1-bkr82",
                    "self_doi": "https://invenio-dev.hcommons-staging.org/doi/10.17613/sdnj1-bkr82",
                    "doi": "https://handle.stage.datacite.org/10.17613/sdnj1-bkr82",
                    "self_iiif_manifest": "https://invenio-dev.hcommons-staging.org/api/iiif/record:sdnj1-bkr82/manifest",
                    "self_iiif_sequence": "https://invenio-dev.hcommons-staging.org/api/iiif/record:sdnj1-bkr82/sequence/default",
                    "files": "https://invenio-dev.hcommons-staging.org/api/records/sdnj1-bkr82/files",
                    "archive": "https://invenio-dev.hcommons-staging.org/api/records/sdnj1-bkr82/files-archive",
                    "latest": "https://invenio-dev.hcommons-staging.org/api/records/sdnj1-bkr82/versions/latest",
                    "latest_html": "https://invenio-dev.hcommons-staging.org/records/sdnj1-bkr82/latest",
                    "draft": "https://invenio-dev.hcommons-staging.org/api/records/sdnj1-bkr82/draft",
                    "versions": "https://invenio-dev.hcommons-staging.org/api/records/sdnj1-bkr82/versions",
                    "access_links": "https://invenio-dev.hcommons-staging.org/api/records/sdnj1-bkr82/access/links",
                    "reserve_doi": "https://invenio-dev.hcommons-staging.org/api/records/sdnj1-bkr82/draft/pids/doi",
                    "communities": "https://invenio-dev.hcommons-staging.org/api/records/sdnj1-bkr82/communities",
                    "communities-suggestions": "https://invenio-dev.hcommons-staging.org/api/records/sdnj1-bkr82/communities-suggestions",
                    "requests": "https://invenio-dev.hcommons-staging.org/api/records/sdnj1-bkr82/requests",
                },
                "revision_id": 3,
                "parent": {"id": "2jjhs-65798", "communities": {}},
                "versions": {"is_latest": true, "index": 1},
                "is_published": true,
                "is_draft": false,
                "pids": {
                    "doi": {
                        "identifier": "10.17613/sdnj1-bkr82",
                        "provider": "datacite",
                        "client": "datacite",
                    },
                    "oai": {
                        "identifier": "oai:invenio-dev.hcommons-staging.org:sdnj1-bkr82",
                        "provider": "oai",
                    },
                },
                "metadata": {
                    "resource_type": {
                        "id": "textDocument-journalArticle",
                        "title": {
                            "de": "Zeitschriftenartikel",
                            "en": "Journal article",
                        },
                    },
                    "creators": [
                        {
                            "person_or_org": {
                                "type": "personal",
                                "name": "Long, Tammy",
                                "given_name": "Tammy",
                                "family_name": "Long",
                            },
                            "role": {"id": "author", "title": {"en": "Author"}},
                        },
                        {
                            "person_or_org": {
                                "type": "personal",
                                "name": "Vasko, Stephanie",
                                "given_name": "Stephanie",
                                "family_name": "Vasko",
                            },
                            "role": {"id": "author", "title": {"en": "Author"}},
                            "affiliations": [{"name": "msu"}],
                        },
                        {
                            "person_or_org": {
                                "type": "personal",
                                "name": "Russell, Bonnie",
                                "given_name": "Bonnie",
                                "family_name": "Russell",
                            },
                            "role": {"id": "author", "title": {"en": "Author"}},
                        },
                        {
                            "person_or_org": {
                                "type": "personal",
                                "name": "Scott, Ian",
                                "given_name": "Ian",
                                "family_name": "Scott",
                            },
                            "role": {"id": "author", "title": {"en": "Author"}},
                        },
                    ],
                    "title": "Invenio: A group process",
                    "publisher": "Mesh Research",
                    "publication_date": "2023-07-28",
                    "identifiers": [
                        {"identifier": "http://www.meshresearch.net", "scheme": "url"}
                    ],
                    "rights": [
                        {
                            "id": "cc-by-4.0",
                            "title": {
                                "en": "Creative Commons Attribution 4.0 International"
                            },
                            "description": {
                                "en": "The Creative Commons Attribution license allows re-distribution and re-use of a licensed work on the condition that the creator is appropriately credited."
                            },
                            "icon": "cc-by-icon",
                            "props": {
                                "url": "https://creativecommons.org/licenses/by/4.0/legalcode",
                                "scheme": "spdx",
                            },
                        }
                    ],
                },
                "custom_fields": {
                    "journal:journal": {
                        "title": "Journal of Invenio Studies",
                        "issue": "1",
                        "volume": "1",
                    },
                    "kcr:ai_usage": {"ai_used": false},
                },
                "access": {
                    "record": "public",
                    "files": "public",
                    "embargo": {"active": false, "reason": null},
                    "status": "open",
                },
                "files": {
                    "enabled": true,
                    "order": [],
                    "count": 1,
                    "total_bytes": 1683773,
                    "entries": {
                        "Invenio Journal Article.pdf": {
                            "ext": "pdf",
                            "key": "Invenio Journal Article.pdf",
                            "metadata": {},
                            "mimetype": "application/pdf",
                            "size": 1683773,
                        }
                    },
                },
                "status": "published",
                "stats": {
                    "this_version": {
                        "views": 0,
                        "unique_views": 0,
                        "downloads": 0,
                        "unique_downloads": 0,
                        "data_volume": 0.0,
                    },
                    "all_versions": {
                        "views": 0,
                        "unique_views": 0,
                        "downloads": 0,
                        "unique_downloads": 0,
                        "data_volume": 0.0,
                    },
                },
            },
            {
                "id": "v38k4-bzw40",
                "created": "2024-02-22T17:19:36.153958+00:00",
                "updated": "2024-02-22T17:19:36.277338+00:00",
                "links": {
                    "self": "https://invenio-dev.hcommons-staging.org/api/records/v38k4-bzw40",
                    "self_html": "https://invenio-dev.hcommons-staging.org/records/v38k4-bzw40",
                    "self_doi": "https://invenio-dev.hcommons-staging.org/doi/10.17613/v38k4-bzw40",
                    "doi": "https://handle.stage.datacite.org/10.17613/v38k4-bzw40",
                    "self_iiif_manifest": "https://invenio-dev.hcommons-staging.org/api/iiif/record:v38k4-bzw40/manifest",
                    "self_iiif_sequence": "https://invenio-dev.hcommons-staging.org/api/iiif/record:v38k4-bzw40/sequence/default",
                    "files": "https://invenio-dev.hcommons-staging.org/api/records/v38k4-bzw40/files",
                    "archive": "https://invenio-dev.hcommons-staging.org/api/records/v38k4-bzw40/files-archive",
                    "latest": "https://invenio-dev.hcommons-staging.org/api/records/v38k4-bzw40/versions/latest",
                    "latest_html": "https://invenio-dev.hcommons-staging.org/records/v38k4-bzw40/latest",
                    "draft": "https://invenio-dev.hcommons-staging.org/api/records/v38k4-bzw40/draft",
                    "versions": "https://invenio-dev.hcommons-staging.org/api/records/v38k4-bzw40/versions",
                    "access_links": "https://invenio-dev.hcommons-staging.org/api/records/v38k4-bzw40/access/links",
                    "reserve_doi": "https://invenio-dev.hcommons-staging.org/api/records/v38k4-bzw40/draft/pids/doi",
                    "communities": "https://invenio-dev.hcommons-staging.org/api/records/v38k4-bzw40/communities",
                    "communities-suggestions": "https://invenio-dev.hcommons-staging.org/api/records/v38k4-bzw40/communities-suggestions",
                    "requests": "https://invenio-dev.hcommons-staging.org/api/records/v38k4-bzw40/requests",
                },
                "revision_id": 3,
                "parent": {"id": "2d9xv-vva49", "communities": {}},
                "versions": {"is_latest": true, "index": 1},
                "is_published": true,
                "is_draft": false,
                "pids": {
                    "doi": {
                        "identifier": "10.17613/v38k4-bzw40",
                        "provider": "datacite",
                        "client": "datacite",
                    },
                    "oai": {
                        "identifier": "oai:invenio-dev.hcommons-staging.org:v38k4-bzw40",
                        "provider": "oai",
                    },
                },
                "metadata": {
                    "resource_type": {
                        "id": "textDocument-journalArticle",
                        "title": {
                            "de": "Zeitschriftenartikel",
                            "en": "Journal article",
                        },
                    },
                    "creators": [
                        {
                            "person_or_org": {
                                "type": "personal",
                                "name": "Babak, Larissa",
                                "given_name": "Larissa",
                                "family_name": "Babak",
                            },
                            "role": {"id": "author", "title": {"en": "Author"}},
                            "affiliations": [{"name": "Michigan State University"}],
                        },
                        {
                            "person_or_org": {
                                "type": "personal",
                                "name": "Vasko, Stephanie",
                                "given_name": "Stephanie",
                                "family_name": "Vasko",
                            },
                            "role": {"id": "author", "title": {"en": "Author"}},
                            "affiliations": [{"name": "Michigan State University"}],
                        },
                        {
                            "person_or_org": {
                                "type": "personal",
                                "name": "Russell, Bonnie",
                                "given_name": "Bonnie",
                                "family_name": "Russell",
                            },
                            "role": {"id": "author", "title": {"en": "Author"}},
                            "affiliations": [{"name": "Michigan State University"}],
                        },
                        {
                            "person_or_org": {
                                "type": "personal",
                                "name": "Scott, Ian",
                                "given_name": "Ian",
                                "family_name": "Scott",
                            },
                            "role": {"id": "author", "title": {"en": "Author"}},
                            "affiliations": [{"name": "Michigan State University"}],
                        },
                    ],
                    "title": "Invenio: A group process",
                    "publisher": "Mesh Research",
                    "publication_date": "2023-07-28",
                    "languages": [{"id": "eng", "title": {"en": "English"}}],
                    "identifiers": [
                        {"identifier": "http://www.meshresearch.net", "scheme": "url"}
                    ],
                    "rights": [
                        {
                            "id": "cc-by-sa-4.0",
                            "title": {
                                "en": "Creative Commons Attribution Share Alike 4.0 International"
                            },
                            "description": {
                                "en": "Permits almost any use subject to providing credit and license notice. Frequently used for media assets and educational materials. The most common license for Open Access scientific publications. Not recommended for software."
                            },
                            "icon": "cc-by-sa-icon",
                            "props": {
                                "url": "https://creativecommons.org/licenses/by-sa/4.0/legalcode",
                                "scheme": "spdx",
                            },
                        }
                    ],
                    "description": "This is my journal article.",
                },
                "custom_fields": {
                    "journal:journal": {
                        "title": "Journal of Invenio Studies",
                        "issue": "1",
                        "volume": "1",
                    },
                    "kcr:user_defined_tags": ["delete-this"],
                    "kcr:ai_usage": {"ai_used": false},
                },
                "access": {
                    "record": "public",
                    "files": "public",
                    "embargo": {"active": false, "reason": null},
                    "status": "open",
                },
                "files": {
                    "enabled": true,
                    "default_preview": "Invenio Journal Article.pdf",
                    "order": [],
                    "count": 1,
                    "total_bytes": 1683773,
                    "entries": {
                        "Invenio Journal Article.pdf": {
                            "ext": "pdf",
                            "key": "Invenio Journal Article.pdf",
                            "metadata": {},
                            "mimetype": "application/pdf",
                            "size": 1683773,
                        }
                    },
                },
                "status": "published",
                "stats": {
                    "this_version": {
                        "views": 0,
                        "unique_views": 0,
                        "downloads": 0,
                        "unique_downloads": 0,
                        "data_volume": 0.0,
                    },
                    "all_versions": {
                        "views": 0,
                        "unique_views": 0,
                        "downloads": 0,
                        "unique_downloads": 0,
                        "data_volume": 0.0,
                    },
                },
            },
            {
                "id": "fsvjw-qnp62",
                "created": "2024-02-22T16:20:34.991515+00:00",
                "updated": "2024-02-22T16:20:35.120646+00:00",
                "links": {
                    "self": "https://invenio-dev.hcommons-staging.org/api/records/fsvjw-qnp62",
                    "self_html": "https://invenio-dev.hcommons-staging.org/records/fsvjw-qnp62",
                    "self_doi": "https://invenio-dev.hcommons-staging.org/doi/10.17613/fsvjw-qnp62",
                    "doi": "https://handle.stage.datacite.org/10.17613/fsvjw-qnp62",
                    "self_iiif_manifest": "https://invenio-dev.hcommons-staging.org/api/iiif/record:fsvjw-qnp62/manifest",
                    "self_iiif_sequence": "https://invenio-dev.hcommons-staging.org/api/iiif/record:fsvjw-qnp62/sequence/default",
                    "files": "https://invenio-dev.hcommons-staging.org/api/records/fsvjw-qnp62/files",
                    "archive": "https://invenio-dev.hcommons-staging.org/api/records/fsvjw-qnp62/files-archive",
                    "latest": "https://invenio-dev.hcommons-staging.org/api/records/fsvjw-qnp62/versions/latest",
                    "latest_html": "https://invenio-dev.hcommons-staging.org/records/fsvjw-qnp62/latest",
                    "draft": "https://invenio-dev.hcommons-staging.org/api/records/fsvjw-qnp62/draft",
                    "versions": "https://invenio-dev.hcommons-staging.org/api/records/fsvjw-qnp62/versions",
                    "access_links": "https://invenio-dev.hcommons-staging.org/api/records/fsvjw-qnp62/access/links",
                    "reserve_doi": "https://invenio-dev.hcommons-staging.org/api/records/fsvjw-qnp62/draft/pids/doi",
                    "communities": "https://invenio-dev.hcommons-staging.org/api/records/fsvjw-qnp62/communities",
                    "communities-suggestions": "https://invenio-dev.hcommons-staging.org/api/records/fsvjw-qnp62/communities-suggestions",
                    "requests": "https://invenio-dev.hcommons-staging.org/api/records/fsvjw-qnp62/requests",
                },
                "revision_id": 3,
                "parent": {"id": "c5hrd-aw913", "communities": {}},
                "versions": {"is_latest": true, "index": 1},
                "is_published": true,
                "is_draft": false,
                "pids": {
                    "doi": {
                        "identifier": "10.17613/fsvjw-qnp62",
                        "provider": "datacite",
                        "client": "datacite",
                    },
                    "oai": {
                        "identifier": "oai:invenio-dev.hcommons-staging.org:fsvjw-qnp62",
                        "provider": "oai",
                    },
                },
                "metadata": {
                    "resource_type": {
                        "id": "textDocument-journalArticle",
                        "title": {
                            "de": "Zeitschriftenartikel",
                            "en": "Journal article",
                        },
                    },
                    "creators": [
                        {
                            "person_or_org": {
                                "type": "personal",
                                "name": "Lee, Kristen",
                                "given_name": "Kristen",
                                "family_name": "Lee",
                            },
                            "role": {"id": "author", "title": {"en": "Author"}},
                        },
                        {
                            "person_or_org": {
                                "type": "personal",
                                "name": "Russell, Bonnie",
                                "given_name": "Bonnie",
                                "family_name": "Russell",
                            },
                            "role": {
                                "id": "collaborator",
                                "title": {"en": "Collaborator"},
                            },
                        },
                        {
                            "person_or_org": {
                                "type": "personal",
                                "name": "Scott, Ian",
                                "given_name": "Ian",
                                "family_name": "Scott",
                            },
                            "role": {
                                "id": "collaborator",
                                "title": {"en": "Collaborator"},
                            },
                        },
                        {
                            "person_or_org": {
                                "type": "personal",
                                "name": "Vasko, Stephanie",
                                "given_name": "Stephanie",
                                "family_name": "Vasko",
                            },
                            "role": {
                                "id": "collaborator",
                                "title": {"en": "Collaborator"},
                            },
                        },
                    ],
                    "title": "Invenio: A group process Research Participant: A. Person",
                    "publisher": "MESH Research",
                    "publication_date": "2023-07-28",
                    "subjects": [
                        {
                            "id": "http://id.worldcat.org/fast/1378126",
                            "subject": "Repository manager/MVS",
                            "scheme": "FAST-title",
                        }
                    ],
                    "identifiers": [
                        {"identifier": "http://www.meshresearch.net", "scheme": "url"}
                    ],
                    "rights": [
                        {
                            "id": "cc-by-4.0",
                            "title": {
                                "en": "Creative Commons Attribution 4.0 International"
                            },
                            "description": {
                                "en": "The Creative Commons Attribution license allows re-distribution and re-use of a licensed work on the condition that the creator is appropriately credited."
                            },
                            "icon": "cc-by-icon",
                            "props": {
                                "url": "https://creativecommons.org/licenses/by/4.0/legalcode",
                                "scheme": "spdx",
                            },
                        }
                    ],
                    "description": "This is where the description of my deposit would go.",
                },
                "custom_fields": {
                    "journal:journal": {
                        "title": "Journal of Invenio Studies",
                        "issue": "1",
                        "volume": "1",
                    },
                    "imprint:imprint": {"place": "Michigan State University"},
                    "kcr:user_defined_tags": ["delete-this"],
                    "kcr:ai_usage": {"ai_used": false},
                },
                "access": {
                    "record": "public",
                    "files": "public",
                    "embargo": {"active": false, "reason": null},
                    "status": "open",
                },
                "files": {
                    "enabled": true,
                    "order": [],
                    "count": 1,
                    "total_bytes": 1683773,
                    "entries": {
                        "Invenio Journal Article.pdf": {
                            "ext": "pdf",
                            "key": "Invenio Journal Article.pdf",
                            "metadata": {},
                            "mimetype": "application/pdf",
                            "size": 1683773,
                        }
                    },
                },
                "status": "published",
                "stats": {
                    "this_version": {
                        "views": 0,
                        "unique_views": 0,
                        "downloads": 0,
                        "unique_downloads": 0,
                        "data_volume": 0.0,
                    },
                    "all_versions": {
                        "views": 0,
                        "unique_views": 0,
                        "downloads": 0,
                        "unique_downloads": 0,
                        "data_volume": 0.0,
                    },
                },
            },
            {
                "id": "bekym-z1916",
                "created": "2024-02-22T14:31:16.671010+00:00",
                "updated": "2024-02-22T14:31:16.793123+00:00",
                "links": {
                    "self": "https://invenio-dev.hcommons-staging.org/api/records/bekym-z1916",
                    "self_html": "https://invenio-dev.hcommons-staging.org/records/bekym-z1916",
                    "self_doi": "https://invenio-dev.hcommons-staging.org/doi/10.17613/bekym-z1916",
                    "doi": "https://handle.stage.datacite.org/10.17613/bekym-z1916",
                    "self_iiif_manifest": "https://invenio-dev.hcommons-staging.org/api/iiif/record:bekym-z1916/manifest",
                    "self_iiif_sequence": "https://invenio-dev.hcommons-staging.org/api/iiif/record:bekym-z1916/sequence/default",
                    "files": "https://invenio-dev.hcommons-staging.org/api/records/bekym-z1916/files",
                    "archive": "https://invenio-dev.hcommons-staging.org/api/records/bekym-z1916/files-archive",
                    "latest": "https://invenio-dev.hcommons-staging.org/api/records/bekym-z1916/versions/latest",
                    "latest_html": "https://invenio-dev.hcommons-staging.org/records/bekym-z1916/latest",
                    "draft": "https://invenio-dev.hcommons-staging.org/api/records/bekym-z1916/draft",
                    "versions": "https://invenio-dev.hcommons-staging.org/api/records/bekym-z1916/versions",
                    "access_links": "https://invenio-dev.hcommons-staging.org/api/records/bekym-z1916/access/links",
                    "reserve_doi": "https://invenio-dev.hcommons-staging.org/api/records/bekym-z1916/draft/pids/doi",
                    "communities": "https://invenio-dev.hcommons-staging.org/api/records/bekym-z1916/communities",
                    "communities-suggestions": "https://invenio-dev.hcommons-staging.org/api/records/bekym-z1916/communities-suggestions",
                    "requests": "https://invenio-dev.hcommons-staging.org/api/records/bekym-z1916/requests",
                },
                "revision_id": 3,
                "parent": {"id": "6a5f2-4x980", "communities": {}},
                "versions": {"is_latest": true, "index": 1},
                "is_published": true,
                "is_draft": false,
                "pids": {
                    "doi": {
                        "identifier": "10.17613/bekym-z1916",
                        "provider": "datacite",
                        "client": "datacite",
                    },
                    "oai": {
                        "identifier": "oai:invenio-dev.hcommons-staging.org:bekym-z1916",
                        "provider": "oai",
                    },
                },
                "metadata": {
                    "resource_type": {
                        "id": "textDocument-journalArticle",
                        "title": {
                            "de": "Zeitschriftenartikel",
                            "en": "Journal article",
                        },
                    },
                    "creators": [
                        {
                            "person_or_org": {
                                "type": "personal",
                                "name": "McKim, Aaron",
                                "given_name": "Aaron",
                                "family_name": "McKim",
                            },
                            "role": {"id": "author", "title": {"en": "Author"}},
                            "affiliations": [{"name": "Michigan State University"}],
                        },
                        {
                            "person_or_org": {
                                "type": "personal",
                                "name": "Vasko, Stephanie",
                                "given_name": "Stephanie",
                                "family_name": "Vasko",
                            },
                            "role": {"id": "author", "title": {"en": "Author"}},
                            "affiliations": [{"name": "Michigan State University"}],
                        },
                        {
                            "person_or_org": {
                                "type": "personal",
                                "name": "Russell, Bonnie",
                                "given_name": "Bonnie",
                                "family_name": "Russell",
                            },
                            "role": {"id": "author", "title": {"en": "Author"}},
                            "affiliations": [{"name": "Michigan State University"}],
                        },
                        {
                            "person_or_org": {
                                "type": "personal",
                                "name": "Scott, Ian",
                                "given_name": "Ian",
                                "family_name": "Scott",
                            },
                            "role": {"id": "author", "title": {"en": "Author"}},
                            "affiliations": [{"name": "Michigan State University"}],
                        },
                    ],
                    "title": "Invenio: A Group Process",
                    "publisher": "Mesh Research",
                    "publication_date": "2023-07-28",
                    "languages": [{"id": "lat", "title": {"en": "Latin"}}],
                    "identifiers": [
                        {"identifier": "http://www.meshresarch.net", "scheme": "url"}
                    ],
                    "rights": [
                        {
                            "id": "apache-2.0",
                            "title": {"en": "Apache License 2.0"},
                            "description": {
                                "en": "A permissive license whose main conditions require preservation of copyright and license notices. Contributors provide an express grant of patent rights. Licensed works, modifications, and larger works may be distributed under different terms and without source code."
                            },
                            "props": {
                                "url": "http://www.apache.org/licenses/LICENSE-2.0",
                                "scheme": "spdx",
                            },
                        }
                    ],
                },
                "custom_fields": {
                    "journal:journal": {
                        "title": "Journal of Invenio Studies",
                        "issue": "1",
                        "volume": "1",
                        "pages": "1-3",
                    }
                },
                "access": {
                    "record": "public",
                    "files": "public",
                    "embargo": {"active": false, "reason": null},
                    "status": "open",
                },
                "files": {
                    "enabled": true,
                    "order": [],
                    "count": 1,
                    "total_bytes": 1683773,
                    "entries": {
                        "Invenio Journal Article.pdf": {
                            "ext": "pdf",
                            "key": "Invenio Journal Article.pdf",
                            "metadata": {},
                            "mimetype": "application/pdf",
                            "size": 1683773,
                        }
                    },
                },
                "status": "published",
                "stats": {
                    "this_version": {
                        "views": 0,
                        "unique_views": 0,
                        "downloads": 0,
                        "unique_downloads": 0,
                        "data_volume": 0.0,
                    },
                    "all_versions": {
                        "views": 0,
                        "unique_views": 0,
                        "downloads": 0,
                        "unique_downloads": 0,
                        "data_volume": 0.0,
                    },
                },
            },
            {
                "id": "6950m-76066",
                "created": "2024-02-20T21:23:33.648350+00:00",
                "updated": "2024-02-20T21:23:33.773877+00:00",
                "links": {
                    "self": "https://invenio-dev.hcommons-staging.org/api/records/6950m-76066",
                    "self_html": "https://invenio-dev.hcommons-staging.org/records/6950m-76066",
                    "self_doi": "https://invenio-dev.hcommons-staging.org/doi/10.17613/6950m-76066",
                    "doi": "https://handle.stage.datacite.org/10.17613/6950m-76066",
                    "self_iiif_manifest": "https://invenio-dev.hcommons-staging.org/api/iiif/record:6950m-76066/manifest",
                    "self_iiif_sequence": "https://invenio-dev.hcommons-staging.org/api/iiif/record:6950m-76066/sequence/default",
                    "files": "https://invenio-dev.hcommons-staging.org/api/records/6950m-76066/files",
                    "archive": "https://invenio-dev.hcommons-staging.org/api/records/6950m-76066/files-archive",
                    "latest": "https://invenio-dev.hcommons-staging.org/api/records/6950m-76066/versions/latest",
                    "latest_html": "https://invenio-dev.hcommons-staging.org/records/6950m-76066/latest",
                    "draft": "https://invenio-dev.hcommons-staging.org/api/records/6950m-76066/draft",
                    "versions": "https://invenio-dev.hcommons-staging.org/api/records/6950m-76066/versions",
                    "access_links": "https://invenio-dev.hcommons-staging.org/api/records/6950m-76066/access/links",
                    "reserve_doi": "https://invenio-dev.hcommons-staging.org/api/records/6950m-76066/draft/pids/doi",
                    "communities": "https://invenio-dev.hcommons-staging.org/api/records/6950m-76066/communities",
                    "communities-suggestions": "https://invenio-dev.hcommons-staging.org/api/records/6950m-76066/communities-suggestions",
                    "requests": "https://invenio-dev.hcommons-staging.org/api/records/6950m-76066/requests",
                },
                "revision_id": 3,
                "parent": {"id": "0fxmb-n4p19", "communities": {}},
                "versions": {"is_latest": true, "index": 1},
                "is_published": true,
                "is_draft": false,
                "pids": {
                    "doi": {
                        "identifier": "10.17613/6950m-76066",
                        "provider": "datacite",
                        "client": "datacite",
                    },
                    "oai": {
                        "identifier": "oai:invenio-dev.hcommons-staging.org:6950m-76066",
                        "provider": "oai",
                    },
                },
                "metadata": {
                    "resource_type": {
                        "id": "textDocument-journalArticle",
                        "title": {
                            "de": "Zeitschriftenartikel",
                            "en": "Journal article",
                        },
                    },
                    "creators": [
                        {
                            "person_or_org": {
                                "type": "personal",
                                "name": "Weber, Penelope",
                                "given_name": "Penelope",
                                "family_name": "Weber",
                            },
                            "role": {"id": "author", "title": {"en": "Author"}},
                            "affiliations": [{"name": "Michigan State University"}],
                        },
                        {
                            "person_or_org": {
                                "type": "personal",
                                "name": "Vasko, Stephanie",
                                "given_name": "Stephanie",
                                "family_name": "Vasko",
                            },
                            "role": {"id": "author", "title": {"en": "Author"}},
                            "affiliations": [{"name": "Mesh Research"}],
                        },
                        {
                            "person_or_org": {
                                "type": "personal",
                                "name": "Russell, Bonnie",
                                "given_name": "Bonnie",
                                "family_name": "Russell",
                            },
                            "role": {"id": "author", "title": {"en": "Author"}},
                            "affiliations": [{"name": "Mesh Research"}],
                        },
                        {
                            "person_or_org": {
                                "type": "personal",
                                "name": "Scott, Ian",
                                "given_name": "Ian",
                                "family_name": "Scott",
                            },
                            "role": {"id": "author", "title": {"en": "Author"}},
                            "affiliations": [{"name": "Michigan State University"}],
                        },
                    ],
                    "title": "Invenio Journal Article",
                    "publisher": "Mesh Research",
                    "publication_date": "2023-07-28",
                    "languages": [{"id": "eng", "title": {"en": "English"}}],
                    "identifiers": [
                        {"identifier": "http://www.meshresearch.net", "scheme": "url"}
                    ],
                    "rights": [
                        {
                            "id": "cc-by-sa-4.0",
                            "title": {
                                "en": "Creative Commons Attribution Share Alike 4.0 International"
                            },
                            "description": {
                                "en": "Permits almost any use subject to providing credit and license notice. Frequently used for media assets and educational materials. The most common license for Open Access scientific publications. Not recommended for software."
                            },
                            "icon": "cc-by-sa-icon",
                            "props": {
                                "url": "https://creativecommons.org/licenses/by-sa/4.0/legalcode",
                                "scheme": "spdx",
                            },
                        }
                    ],
                    "description": "A journal article written as a test for this system.",
                },
                "custom_fields": {
                    "journal:journal": {
                        "title": "Journal of Invenio Studies",
                        "issue": "1",
                        "volume": "1",
                        "pages": "3",
                    },
                    "imprint:imprint": {"place": "Michigan State University"},
                    "kcr:user_defined_tags": ["delete-this"],
                    "kcr:ai_usage": {"ai_used": false},
                },
                "access": {
                    "record": "public",
                    "files": "public",
                    "embargo": {"active": false, "reason": null},
                    "status": "open",
                },
                "files": {
                    "enabled": true,
                    "order": [],
                    "count": 1,
                    "total_bytes": 1683773,
                    "entries": {
                        "Invenio Journal Article.pdf": {
                            "ext": "pdf",
                            "key": "Invenio Journal Article.pdf",
                            "metadata": {},
                            "mimetype": "application/pdf",
                            "size": 1683773,
                        }
                    },
                },
                "status": "published",
                "stats": {
                    "this_version": {
                        "views": 0,
                        "unique_views": 0,
                        "downloads": 0,
                        "unique_downloads": 0,
                        "data_volume": 0.0,
                    },
                    "all_versions": {
                        "views": 0,
                        "unique_views": 0,
                        "downloads": 0,
                        "unique_downloads": 0,
                        "data_volume": 0.0,
                    },
                },
            },
            {
                "id": "x0ahx-fva39",
                "created": "2024-02-16T16:20:18.522773+00:00",
                "updated": "2024-02-16T16:20:18.852997+00:00",
                "links": {
                    "self": "https://invenio-dev.hcommons-staging.org/api/records/x0ahx-fva39",
                    "self_html": "https://invenio-dev.hcommons-staging.org/records/x0ahx-fva39",
                    "self_doi": "https://invenio-dev.hcommons-staging.org/doi/10.17613/x0ahx-fva39",
                    "doi": "https://handle.stage.datacite.org/10.17613/x0ahx-fva39",
                    "self_iiif_manifest": "https://invenio-dev.hcommons-staging.org/api/iiif/record:x0ahx-fva39/manifest",
                    "self_iiif_sequence": "https://invenio-dev.hcommons-staging.org/api/iiif/record:x0ahx-fva39/sequence/default",
                    "files": "https://invenio-dev.hcommons-staging.org/api/records/x0ahx-fva39/files",
                    "archive": "https://invenio-dev.hcommons-staging.org/api/records/x0ahx-fva39/files-archive",
                    "latest": "https://invenio-dev.hcommons-staging.org/api/records/x0ahx-fva39/versions/latest",
                    "latest_html": "https://invenio-dev.hcommons-staging.org/records/x0ahx-fva39/latest",
                    "draft": "https://invenio-dev.hcommons-staging.org/api/records/x0ahx-fva39/draft",
                    "versions": "https://invenio-dev.hcommons-staging.org/api/records/x0ahx-fva39/versions",
                    "access_links": "https://invenio-dev.hcommons-staging.org/api/records/x0ahx-fva39/access/links",
                    "reserve_doi": "https://invenio-dev.hcommons-staging.org/api/records/x0ahx-fva39/draft/pids/doi",
                    "communities": "https://invenio-dev.hcommons-staging.org/api/records/x0ahx-fva39/communities",
                    "communities-suggestions": "https://invenio-dev.hcommons-staging.org/api/records/x0ahx-fva39/communities-suggestions",
                    "requests": "https://invenio-dev.hcommons-staging.org/api/records/x0ahx-fva39/requests",
                },
                "revision_id": 3,
                "parent": {"id": "v4m5k-2n279", "communities": {}},
                "versions": {"is_latest": true, "index": 1},
                "is_published": true,
                "is_draft": false,
                "pids": {
                    "doi": {
                        "identifier": "10.17613/x0ahx-fva39",
                        "provider": "datacite",
                        "client": "datacite",
                    },
                    "oai": {
                        "identifier": "oai:invenio-dev.hcommons-staging.org:x0ahx-fva39",
                        "provider": "oai",
                    },
                },
                "metadata": {
                    "resource_type": {
                        "id": "textDocument-journalArticle",
                        "title": {
                            "de": "Zeitschriftenartikel",
                            "en": "Journal article",
                        },
                    },
                    "creators": [
                        {
                            "person_or_org": {
                                "type": "personal",
                                "name": "Test, Juno",
                                "given_name": "Juno",
                                "family_name": "Test",
                            },
                            "role": {"id": "author", "title": {"en": "Author"}},
                        },
                        {
                            "person_or_org": {
                                "type": "personal",
                                "name": "Vasko, Stephanie",
                                "given_name": "Stephanie",
                                "family_name": "Vasko",
                            },
                            "role": {"id": "author", "title": {"en": "Author"}},
                        },
                        {
                            "person_or_org": {
                                "type": "personal",
                                "name": "Russell, Bonnie",
                                "given_name": "Bonnie",
                                "family_name": "Russell",
                            },
                            "role": {"id": "author", "title": {"en": "Author"}},
                        },
                        {
                            "person_or_org": {
                                "type": "personal",
                                "name": "Scott, Ian",
                                "given_name": "Ian",
                                "family_name": "Scott",
                            },
                            "role": {"id": "author", "title": {"en": "Author"}},
                        },
                    ],
                    "title": "Invenio: A group process",
                    "publisher": "Mesh Research",
                    "publication_date": "2023-07-28",
                    "subjects": [
                        {
                            "id": "http://id.worldcat.org/fast/997945",
                            "subject": "Library science--Library resources",
                            "scheme": "FAST-topical",
                        }
                    ],
                    "languages": [{"id": "eng", "title": {"en": "English"}}],
                    "identifiers": [
                        {"identifier": "https://meshresearch.net", "scheme": "url"}
                    ],
                    "rights": [
                        {
                            "id": "cc-by-4.0",
                            "title": {
                                "en": "Creative Commons Attribution 4.0 International"
                            },
                            "description": {
                                "en": "The Creative Commons Attribution license allows re-distribution and re-use of a licensed work on the condition that the creator is appropriately credited."
                            },
                            "icon": "cc-by-icon",
                            "props": {
                                "url": "https://creativecommons.org/licenses/by/4.0/legalcode",
                                "scheme": "spdx",
                            },
                        }
                    ],
                    "description": "This is a journal article.",
                },
                "custom_fields": {
                    "journal:journal": {"title": "Invenio: A Journal"},
                    "kcr:user_defined_tags": ["delete-this"],
                    "kcr:ai_usage": {"ai_used": false},
                },
                "access": {
                    "record": "public",
                    "files": "public",
                    "embargo": {"active": false, "reason": null},
                    "status": "open",
                },
                "files": {
                    "enabled": true,
                    "order": [],
                    "count": 1,
                    "total_bytes": 1683773,
                    "entries": {
                        "Invenio Journal Article.pdf": {
                            "ext": "pdf",
                            "key": "Invenio Journal Article.pdf",
                            "metadata": {},
                            "mimetype": "application/pdf",
                            "size": 1683773,
                        }
                    },
                },
                "status": "published",
                "stats": {
                    "this_version": {
                        "views": 0,
                        "unique_views": 0,
                        "downloads": 0,
                        "unique_downloads": 0,
                        "data_volume": 0.0,
                    },
                    "all_versions": {
                        "views": 0,
                        "unique_views": 0,
                        "downloads": 0,
                        "unique_downloads": 0,
                        "data_volume": 0.0,
                    },
                },
            },
            {
                "id": "ge0ap-44q20",
                "created": "2024-02-02T21:54:21.779555+00:00",
                "updated": "2024-02-02T21:54:21.903387+00:00",
                "links": {
                    "self": "https://invenio-dev.hcommons-staging.org/api/records/ge0ap-44q20",
                    "self_html": "https://invenio-dev.hcommons-staging.org/records/ge0ap-44q20",
                    "self_doi": "https://invenio-dev.hcommons-staging.org/doi/10.17613/ge0ap-44q20",
                    "doi": "https://handle.stage.datacite.org/10.17613/ge0ap-44q20",
                    "self_iiif_manifest": "https://invenio-dev.hcommons-staging.org/api/iiif/record:ge0ap-44q20/manifest",
                    "self_iiif_sequence": "https://invenio-dev.hcommons-staging.org/api/iiif/record:ge0ap-44q20/sequence/default",
                    "files": "https://invenio-dev.hcommons-staging.org/api/records/ge0ap-44q20/files",
                    "archive": "https://invenio-dev.hcommons-staging.org/api/records/ge0ap-44q20/files-archive",
                    "latest": "https://invenio-dev.hcommons-staging.org/api/records/ge0ap-44q20/versions/latest",
                    "latest_html": "https://invenio-dev.hcommons-staging.org/records/ge0ap-44q20/latest",
                    "draft": "https://invenio-dev.hcommons-staging.org/api/records/ge0ap-44q20/draft",
                    "versions": "https://invenio-dev.hcommons-staging.org/api/records/ge0ap-44q20/versions",
                    "access_links": "https://invenio-dev.hcommons-staging.org/api/records/ge0ap-44q20/access/links",
                    "reserve_doi": "https://invenio-dev.hcommons-staging.org/api/records/ge0ap-44q20/draft/pids/doi",
                    "communities": "https://invenio-dev.hcommons-staging.org/api/records/ge0ap-44q20/communities",
                    "communities-suggestions": "https://invenio-dev.hcommons-staging.org/api/records/ge0ap-44q20/communities-suggestions",
                    "requests": "https://invenio-dev.hcommons-staging.org/api/records/ge0ap-44q20/requests",
                },
                "revision_id": 3,
                "parent": {"id": "sc620-7pr06", "communities": {}},
                "versions": {"is_latest": true, "index": 1},
                "is_published": true,
                "is_draft": false,
                "pids": {
                    "oai": {
                        "identifier": "oai:invenio-dev.hcommons-staging.org:ge0ap-44q20",
                        "provider": "oai",
                    },
                    "doi": {
                        "identifier": "10.17613/ge0ap-44q20",
                        "provider": "datacite",
                        "client": "datacite",
                    },
                },
                "metadata": {
                    "resource_type": {
                        "id": "audiovisual-podcastEpisode",
                        "title": {"de": "Podcast", "en": "Podcast episode"},
                    },
                    "creators": [
                        {
                            "person_or_org": {
                                "type": "personal",
                                "name": "Russell, Bonnie",
                                "given_name": "Bonnie",
                                "family_name": "Russell",
                            },
                            "role": {"id": "author", "title": {"en": "Author"}},
                        }
                    ],
                    "title": "Weird Medieval Guys",
                    "publisher": "self",
                    "publication_date": "2024-01-02",
                    "subjects": [
                        {
                            "id": "http://id.worldcat.org/fast/1787015",
                            "subject": "Medieval",
                            "scheme": "FAST-title",
                        },
                        {
                            "id": "http://id.worldcat.org/fast/1361587",
                            "subject": "Weird tales",
                            "scheme": "FAST-title",
                        },
                    ],
                    "languages": [{"id": "eng", "title": {"en": "English"}}],
                    "identifiers": [
                        {
                            "identifier": "https://www.instagram.com/weirdmedievalguys/",
                            "scheme": "url",
                        }
                    ],
                    "sizes": ["1 hour and 20 minutes"],
                    "rights": [
                        {
                            "id": "cc-by-4.0",
                            "title": {
                                "en": "Creative Commons Attribution 4.0 International"
                            },
                            "description": {
                                "en": "The Creative Commons Attribution license allows re-distribution and re-use of a licensed work on the condition that the creator is appropriately credited."
                            },
                            "icon": "cc-by-icon",
                            "props": {
                                "url": "https://creativecommons.org/licenses/by/4.0/legalcode",
                                "scheme": "spdx",
                            },
                        }
                    ],
                    "description": "If you love Weird Medieval Guys this is the podcast for you.",
                },
                "custom_fields": {
                    "imprint:imprint": {"place": "Camelot"},
                    "kcr:content_warning": "Some conversation concerns not safe for work topics.",
                    "kcr:project_title": "Weird Medieval Guys",
                    "kcr:publication_url": "https://www.instagram.com/weirdmedievalguys/",
                    "kcr:user_defined_tags": ["Marginalia", "drawings"],
                    "kcr:ai_usage": {"ai_used": false},
                },
                "access": {
                    "record": "public",
                    "files": "public",
                    "embargo": {"active": false, "reason": null},
                    "status": "open",
                },
                "files": {
                    "enabled": true,
                    "order": [],
                    "count": 1,
                    "total_bytes": 1222,
                    "entries": {
                        "file_example_MP3_5MG.mp3": {
                            "ext": "mp3",
                            "key": "file_example_MP3_5MG.mp3",
                            "metadata": {},
                            "mimetype": "audio/mpeg",
                            "size": 1222,
                        }
                    },
                },
                "status": "published",
                "stats": {
                    "this_version": {
                        "views": 0,
                        "unique_views": 0,
                        "downloads": 0,
                        "unique_downloads": 0,
                        "data_volume": 0.0,
                    },
                    "all_versions": {
                        "views": 0,
                        "unique_views": 0,
                        "downloads": 0,
                        "unique_downloads": 0,
                        "data_volume": 0.0,
                    },
                },
            },
            {
                "id": "jd25g-8j271",
                "created": "2024-02-02T21:04:11.408348+00:00",
                "updated": "2024-02-02T21:04:11.519109+00:00",
                "links": {
                    "self": "https://invenio-dev.hcommons-staging.org/api/records/jd25g-8j271",
                    "self_html": "https://invenio-dev.hcommons-staging.org/records/jd25g-8j271",
                    "self_doi": "https://invenio-dev.hcommons-staging.org/doi/10.17613/jd25g-8j271",
                    "doi": "https://handle.stage.datacite.org/10.17613/jd25g-8j271",
                    "self_iiif_manifest": "https://invenio-dev.hcommons-staging.org/api/iiif/record:jd25g-8j271/manifest",
                    "self_iiif_sequence": "https://invenio-dev.hcommons-staging.org/api/iiif/record:jd25g-8j271/sequence/default",
                    "files": "https://invenio-dev.hcommons-staging.org/api/records/jd25g-8j271/files",
                    "archive": "https://invenio-dev.hcommons-staging.org/api/records/jd25g-8j271/files-archive",
                    "latest": "https://invenio-dev.hcommons-staging.org/api/records/jd25g-8j271/versions/latest",
                    "latest_html": "https://invenio-dev.hcommons-staging.org/records/jd25g-8j271/latest",
                    "draft": "https://invenio-dev.hcommons-staging.org/api/records/jd25g-8j271/draft",
                    "versions": "https://invenio-dev.hcommons-staging.org/api/records/jd25g-8j271/versions",
                    "access_links": "https://invenio-dev.hcommons-staging.org/api/records/jd25g-8j271/access/links",
                    "reserve_doi": "https://invenio-dev.hcommons-staging.org/api/records/jd25g-8j271/draft/pids/doi",
                    "communities": "https://invenio-dev.hcommons-staging.org/api/records/jd25g-8j271/communities",
                    "communities-suggestions": "https://invenio-dev.hcommons-staging.org/api/records/jd25g-8j271/communities-suggestions",
                    "requests": "https://invenio-dev.hcommons-staging.org/api/records/jd25g-8j271/requests",
                },
                "revision_id": 3,
                "parent": {"id": "wcdhe-htj05", "communities": {}},
                "versions": {"is_latest": true, "index": 1},
                "is_published": true,
                "is_draft": false,
                "pids": {
                    "oai": {
                        "identifier": "oai:invenio-dev.hcommons-staging.org:jd25g-8j271",
                        "provider": "oai",
                    },
                    "doi": {
                        "identifier": "10.17613/jd25g-8j271",
                        "provider": "datacite",
                        "client": "datacite",
                    },
                },
                "metadata": {
                    "resource_type": {
                        "id": "textDocument-journalArticle",
                        "title": {
                            "de": "Zeitschriftenartikel",
                            "en": "Journal article",
                        },
                    },
                    "creators": [
                        {
                            "person_or_org": {
                                "type": "personal",
                                "name": "Russell, Bonnie",
                                "given_name": "Bonnie",
                                "family_name": "Russell",
                            },
                            "role": {"id": "author", "title": {"en": "Author"}},
                            "affiliations": [{"name": "Michigan State University"}],
                        }
                    ],
                    "title": "Mastodon 101",
                    "publisher": "self",
                    "publication_date": "2024-02-02",
                    "subjects": [
                        {
                            "id": "http://id.worldcat.org/fast/1741098",
                            "subject": "Social media",
                            "scheme": "FAST-topical",
                        },
                        {
                            "id": "http://id.worldcat.org/fast/1011599",
                            "subject": "Mastodon",
                            "scheme": "FAST-topical",
                        },
                    ],
                    "languages": [{"id": "eng", "title": {"en": "English"}}],
                    "description": "Your guide to finding a home on Mastodon.",
                },
                "custom_fields": {
                    "journal:journal": {
                        "title": "Mastodon Central",
                        "issue": "1",
                        "volume": "1",
                    },
                    "kcr:user_defined_tags": ["fediverse"],
                    "kcr:ai_usage": {"ai_used": false},
                },
                "access": {
                    "record": "public",
                    "files": "public",
                    "embargo": {"active": false, "reason": null},
                    "status": "open",
                },
                "files": {
                    "enabled": true,
                    "order": [],
                    "count": 1,
                    "total_bytes": 83873,
                    "entries": {
                        "mastodon-101.pdf": {
                            "ext": "pdf",
                            "key": "mastodon-101.pdf",
                            "metadata": {},
                            "mimetype": "application/pdf",
                            "size": 83873,
                        }
                    },
                },
                "status": "published",
                "stats": {
                    "this_version": {
                        "views": 0,
                        "unique_views": 0,
                        "downloads": 0,
                        "unique_downloads": 0,
                        "data_volume": 0.0,
                    },
                    "all_versions": {
                        "views": 0,
                        "unique_views": 0,
                        "downloads": 0,
                        "unique_downloads": 0,
                        "data_volume": 0.0,
                    },
                },
            },
            {
                "id": "vwsxw-t4b63",
                "created": "2024-02-02T19:10:41.652006+00:00",
                "updated": "2024-02-02T19:10:41.762164+00:00",
                "links": {
                    "self": "https://invenio-dev.hcommons-staging.org/api/records/vwsxw-t4b63",
                    "self_html": "https://invenio-dev.hcommons-staging.org/records/vwsxw-t4b63",
                    "self_doi": "https://invenio-dev.hcommons-staging.org/doi/10.17613/vwsxw-t4b63",
                    "doi": "https://handle.stage.datacite.org/10.17613/vwsxw-t4b63",
                    "self_iiif_manifest": "https://invenio-dev.hcommons-staging.org/api/iiif/record:vwsxw-t4b63/manifest",
                    "self_iiif_sequence": "https://invenio-dev.hcommons-staging.org/api/iiif/record:vwsxw-t4b63/sequence/default",
                    "files": "https://invenio-dev.hcommons-staging.org/api/records/vwsxw-t4b63/files",
                    "archive": "https://invenio-dev.hcommons-staging.org/api/records/vwsxw-t4b63/files-archive",
                    "latest": "https://invenio-dev.hcommons-staging.org/api/records/vwsxw-t4b63/versions/latest",
                    "latest_html": "https://invenio-dev.hcommons-staging.org/records/vwsxw-t4b63/latest",
                    "draft": "https://invenio-dev.hcommons-staging.org/api/records/vwsxw-t4b63/draft",
                    "versions": "https://invenio-dev.hcommons-staging.org/api/records/vwsxw-t4b63/versions",
                    "access_links": "https://invenio-dev.hcommons-staging.org/api/records/vwsxw-t4b63/access/links",
                    "reserve_doi": "https://invenio-dev.hcommons-staging.org/api/records/vwsxw-t4b63/draft/pids/doi",
                    "communities": "https://invenio-dev.hcommons-staging.org/api/records/vwsxw-t4b63/communities",
                    "communities-suggestions": "https://invenio-dev.hcommons-staging.org/api/records/vwsxw-t4b63/communities-suggestions",
                    "requests": "https://invenio-dev.hcommons-staging.org/api/records/vwsxw-t4b63/requests",
                },
                "revision_id": 3,
                "parent": {"id": "xf1nq-f6247", "communities": {}},
                "versions": {"is_latest": true, "index": 1},
                "is_published": true,
                "is_draft": false,
                "pids": {
                    "oai": {
                        "identifier": "oai:invenio-dev.hcommons-staging.org:vwsxw-t4b63",
                        "provider": "oai",
                    },
                    "doi": {
                        "identifier": "10.17613/vwsxw-t4b63",
                        "provider": "datacite",
                        "client": "datacite",
                    },
                },
                "metadata": {
                    "resource_type": {
                        "id": "audiovisual-podcastEpisode",
                        "title": {"de": "Podcast", "en": "Podcast episode"},
                    },
                    "creators": [
                        {
                            "person_or_org": {
                                "type": "personal",
                                "name": "Rand Test",
                                "family_name": "Rand Test",
                            },
                            "role": {"id": "author", "title": {"en": "Author"}},
                        },
                        {
                            "person_or_org": {
                                "type": "personal",
                                "name": "Russell, Bonnie",
                                "given_name": "Bonnie",
                                "family_name": "Russell",
                            },
                            "role": {"id": "author", "title": {"en": "Author"}},
                        },
                    ],
                    "title": "TEST AUDIO",
                    "publisher": "self",
                    "publication_date": "2024-02-02",
                    "rights": [
                        {
                            "id": "cc-by-sa-4.0",
                            "title": {
                                "en": "Creative Commons Attribution Share Alike 4.0 International"
                            },
                            "description": {
                                "en": "Permits almost any use subject to providing credit and license notice. Frequently used for media assets and educational materials. The most common license for Open Access scientific publications. Not recommended for software."
                            },
                            "icon": "cc-by-sa-icon",
                            "props": {
                                "url": "https://creativecommons.org/licenses/by-sa/4.0/legalcode",
                                "scheme": "spdx",
                            },
                        }
                    ],
                },
                "custom_fields": {
                    "kcr:user_defined_tags": ["delete-this"],
                    "kcr:ai_usage": {"ai_used": false},
                },
                "access": {
                    "record": "public",
                    "files": "public",
                    "embargo": {"active": false, "reason": null},
                    "status": "open",
                },
                "files": {
                    "enabled": true,
                    "order": [],
                    "count": 1,
                    "total_bytes": 571424,
                    "entries": {
                        "test.m4a": {
                            "ext": "m4a",
                            "key": "test.m4a",
                            "metadata": {},
                            "mimetype": "audio/mp4",
                            "size": 571424,
                        }
                    },
                },
                "status": "published",
                "stats": {
                    "this_version": {
                        "views": 0,
                        "unique_views": 0,
                        "downloads": 0,
                        "unique_downloads": 0,
                        "data_volume": 0.0,
                    },
                    "all_versions": {
                        "views": 0,
                        "unique_views": 0,
                        "downloads": 0,
                        "unique_downloads": 0,
                        "data_volume": 0.0,
                    },
                },
            },
            {
                "id": "5xf3c-khf14",
                "created": "2024-02-02T18:47:04.154789+00:00",
                "updated": "2024-02-02T18:47:04.272281+00:00",
                "links": {
                    "self": "https://invenio-dev.hcommons-staging.org/api/records/5xf3c-khf14",
                    "self_html": "https://invenio-dev.hcommons-staging.org/records/5xf3c-khf14",
                    "self_doi": "https://invenio-dev.hcommons-staging.org/doi/10.17613/M63N8N",
                    "doi": "https://handle.stage.datacite.org/10.17613/M63N8N",
                    "self_iiif_manifest": "https://invenio-dev.hcommons-staging.org/api/iiif/record:5xf3c-khf14/manifest",
                    "self_iiif_sequence": "https://invenio-dev.hcommons-staging.org/api/iiif/record:5xf3c-khf14/sequence/default",
                    "files": "https://invenio-dev.hcommons-staging.org/api/records/5xf3c-khf14/files",
                    "archive": "https://invenio-dev.hcommons-staging.org/api/records/5xf3c-khf14/files-archive",
                    "latest": "https://invenio-dev.hcommons-staging.org/api/records/5xf3c-khf14/versions/latest",
                    "latest_html": "https://invenio-dev.hcommons-staging.org/records/5xf3c-khf14/latest",
                    "draft": "https://invenio-dev.hcommons-staging.org/api/records/5xf3c-khf14/draft",
                    "versions": "https://invenio-dev.hcommons-staging.org/api/records/5xf3c-khf14/versions",
                    "access_links": "https://invenio-dev.hcommons-staging.org/api/records/5xf3c-khf14/access/links",
                    "reserve_doi": "https://invenio-dev.hcommons-staging.org/api/records/5xf3c-khf14/draft/pids/doi",
                    "communities": "https://invenio-dev.hcommons-staging.org/api/records/5xf3c-khf14/communities",
                    "communities-suggestions": "https://invenio-dev.hcommons-staging.org/api/records/5xf3c-khf14/communities-suggestions",
                    "requests": "https://invenio-dev.hcommons-staging.org/api/records/5xf3c-khf14/requests",
                },
                "revision_id": 3,
                "parent": {
                    "id": "gxgg8-v9m69",
                    "communities": {
                        "ids": ["6060e26c-54e3-4f33-8710-1bb89d3672ea"],
                        "default": "6060e26c-54e3-4f33-8710-1bb89d3672ea",
                    },
                },
                "versions": {"is_latest": true, "index": 1},
                "is_published": true,
                "is_draft": false,
                "pids": {
                    "doi": {
                        "identifier": "10.17613/M63N8N",
                        "provider": "datacite",
                        "client": "datacite",
                    },
                    "oai": {
                        "identifier": "oai:invenio-dev.hcommons-staging.org:5xf3c-khf14",
                        "provider": "oai",
                    },
                },
                "metadata": {
                    "resource_type": {
                        "id": "textDocument-journalArticle",
                        "title": {
                            "de": "Zeitschriftenartikel",
                            "en": "Journal article",
                        },
                    },
                    "creators": [
                        {
                            "person_or_org": {
                                "type": "personal",
                                "name": "Dorf, Samuel",
                                "given_name": "Samuel",
                                "family_name": "Dorf",
                                "identifiers": [
                                    {"identifier": "sdorf", "scheme": "hc_username"}
                                ],
                            },
                            "role": {"id": "author", "title": {"en": "Author"}},
                        }
                    ],
                    "title": "Listening in Hard Times: Music for Struggle and Solace",
                    "publisher": "Published by the Institute on Inequality at UCLA Luskin",
                    "publication_date": "2017",
                    "subjects": [
                        {
                            "id": "http://id.worldcat.org/fast/1030893",
                            "subject": "Musicology",
                            "scheme": "FAST-topical",
                        }
                    ],
                    "languages": [{"id": "eng", "title": {"en": "English"}}],
                    "identifiers": [
                        {"identifier": "hc:16863", "scheme": "hclegacy-pid"},
                        {"identifier": "1000360-9855", "scheme": "hclegacy-record-id"},
                        {"identifier": "10.17613/M63N8N", "scheme": "datacite-doi"},
                        {
                            "identifier": "https://issuu.com/uclapubaffairs/docs/j18-teach-organize-resist",
                            "scheme": "url",
                        },
                    ],
                    "rights": [
                        {
                            "id": "arr",
                            "title": {"en": "All Rights Reserved"},
                            "description": {
                                "en": "Proprietary material. No permissions are granted for any kind of copyring or re-use. All rights reserved"
                            },
                            "icon": "copyright",
                            "props": {
                                "url": "https://en.wikipedia.org/wiki/All_rights_reserved"
                            },
                        }
                    ],
                    "description": "Talk on Beyoncé's Lemonade and ANOHNI's Hopelessness",
                },
                "custom_fields": {
                    "journal:journal": {"title": "#J18 Teach.Organize.Resist."},
                    "kcr:commons_domain": "hcommons.org",
                    "kcr:submitter_email": "Samuel.Dorf@gmail.com",
                    "kcr:submitter_username": "sdorf",
                    "kcr:notes": "https://issuu.com/uclapubaffairs/docs/j18-teach-organize-resist",
                    "kcr:user_defined_tags": ["ANOHNI", "Beyoncé"],
                    "hclegacy:collection": "hccollection:1",
                    "hclegacy:file_location": "/srv/www/commons/current/web/app/uploads/humcore/2017/12/o_1c0pv594b1n4ot0d9u9t81jkr7.pdf.dorf-listening-in-hard-times-2017.pdf",
                    "hclegacy:file_pid": "hc:16864",
                    "hclegacy:previously_published": "published",
                    "hclegacy:publication_type": "online-publication",
                    "hclegacy:record_change_date": "2017-12-08T02:32:04Z",
                    "hclegacy:record_creation_date": "2017-12-08T02:32:04Z",
                    "hclegacy:submitter_org_memberships": ["hc"],
                    "hclegacy:submitter_id": "1010942",
                },
                "access": {
                    "record": "public",
                    "files": "public",
                    "embargo": {"active": false, "reason": null},
                    "status": "open",
                },
                "files": {
                    "enabled": true,
                    "order": [],
                    "count": 1,
                    "total_bytes": 2635791,
                    "entries": {
                        "dorf-listening-in-hard-times-2017.pdf": {
                            "ext": "pdf",
                            "key": "dorf-listening-in-hard-times-2017.pdf",
                            "metadata": {},
                            "mimetype": "application/pdf",
                            "size": 2635791,
                        }
                    },
                },
                "status": "published",
                "stats": {
                    "this_version": {
                        "views": 0,
                        "unique_views": 0,
                        "downloads": 0,
                        "unique_downloads": 0,
                        "data_volume": 0.0,
                    },
                    "all_versions": {
                        "views": 0,
                        "unique_views": 0,
                        "downloads": 0,
                        "unique_downloads": 0,
                        "data_volume": 0.0,
                    },
                },
            },
            {
                "id": "dn7qw-yqk29",
                "created": "2024-02-02T18:43:55.039419+00:00",
                "updated": "2024-02-02T18:43:55.174523+00:00",
                "links": {
                    "self": "https://invenio-dev.hcommons-staging.org/api/records/dn7qw-yqk29",
                    "self_html": "https://invenio-dev.hcommons-staging.org/records/dn7qw-yqk29",
                    "self_doi": "https://invenio-dev.hcommons-staging.org/doi/10.17613/M6F790",
                    "doi": "https://handle.stage.datacite.org/10.17613/M6F790",
                    "self_iiif_manifest": "https://invenio-dev.hcommons-staging.org/api/iiif/record:dn7qw-yqk29/manifest",
                    "self_iiif_sequence": "https://invenio-dev.hcommons-staging.org/api/iiif/record:dn7qw-yqk29/sequence/default",
                    "files": "https://invenio-dev.hcommons-staging.org/api/records/dn7qw-yqk29/files",
                    "archive": "https://invenio-dev.hcommons-staging.org/api/records/dn7qw-yqk29/files-archive",
                    "latest": "https://invenio-dev.hcommons-staging.org/api/records/dn7qw-yqk29/versions/latest",
                    "latest_html": "https://invenio-dev.hcommons-staging.org/records/dn7qw-yqk29/latest",
                    "draft": "https://invenio-dev.hcommons-staging.org/api/records/dn7qw-yqk29/draft",
                    "versions": "https://invenio-dev.hcommons-staging.org/api/records/dn7qw-yqk29/versions",
                    "access_links": "https://invenio-dev.hcommons-staging.org/api/records/dn7qw-yqk29/access/links",
                    "reserve_doi": "https://invenio-dev.hcommons-staging.org/api/records/dn7qw-yqk29/draft/pids/doi",
                    "communities": "https://invenio-dev.hcommons-staging.org/api/records/dn7qw-yqk29/communities",
                    "communities-suggestions": "https://invenio-dev.hcommons-staging.org/api/records/dn7qw-yqk29/communities-suggestions",
                    "requests": "https://invenio-dev.hcommons-staging.org/api/records/dn7qw-yqk29/requests",
                },
                "revision_id": 3,
                "parent": {
                    "id": "46hev-9sn30",
                    "communities": {
                        "ids": ["6060e26c-54e3-4f33-8710-1bb89d3672ea"],
                        "default": "6060e26c-54e3-4f33-8710-1bb89d3672ea",
                    },
                },
                "versions": {"is_latest": true, "index": 1},
                "is_published": true,
                "is_draft": false,
                "pids": {
                    "doi": {
                        "identifier": "10.17613/M6F790",
                        "provider": "datacite",
                        "client": "datacite",
                    },
                    "oai": {
                        "identifier": "oai:invenio-dev.hcommons-staging.org:dn7qw-yqk29",
                        "provider": "oai",
                    },
                },
                "metadata": {
                    "resource_type": {
                        "id": "textDocument-review",
                        "title": {"de": "Rezension", "en": "Review"},
                    },
                    "creators": [
                        {
                            "person_or_org": {
                                "type": "personal",
                                "name": "Chattopadhyay, Subhasis",
                                "given_name": "Subhasis",
                                "family_name": "Chattopadhyay",
                                "identifiers": [
                                    {"identifier": "subhasis", "scheme": "hc_username"}
                                ],
                            },
                            "role": {"id": "author", "title": {"en": "Author"}},
                        }
                    ],
                    "title": "Review of Julia Kristeva's This Incredible Need to Believe",
                    "publisher": "unknown",
                    "publication_date": "2017",
                    "subjects": [
                        {
                            "id": "http://id.worldcat.org/fast/1081551",
                            "subject": "Psychology and literature",
                            "scheme": "FAST-topical",
                        },
                        {
                            "id": "http://id.worldcat.org/fast/1081152",
                            "subject": "Psychiatry",
                            "scheme": "FAST-topical",
                        },
                    ],
                    "dates": [
                        {
                            "date": "2017-10-01",
                            "type": {
                                "id": "issued",
                                "title": {"de": "Veröffentlicht", "en": "Issued"},
                            },
                            "description": "Publication date",
                        }
                    ],
                    "languages": [{"id": "eng", "title": {"en": "English"}}],
                    "identifiers": [
                        {"identifier": "hc:15827", "scheme": "hclegacy-pid"},
                        {"identifier": "1000360-8357", "scheme": "hclegacy-record-id"},
                        {"identifier": "10.17613/M6F790", "scheme": "datacite-doi"},
                        {
                            "identifier": "https://doi.org/10.17613/M6F790",
                            "scheme": "url",
                        },
                    ],
                    "rights": [
                        {
                            "id": "cc-by-nc-sa-4.0",
                            "title": {
                                "en": "Creative Commons Attribution Non Commercial Share Alike 4.0 International"
                            },
                            "description": {"en": ""},
                            "icon": "cc-by-nc-sa-icon",
                            "props": {
                                "url": "https://creativecommons.org/licenses/by-nc-sa/4.0/legalcode",
                                "scheme": "spdx",
                            },
                        }
                    ],
                    "description": "This reviewer had read Kristeva in October, 2016 in this Journal (and the review is freely available online and had garnered some small publicity). Over the last one year this reviewer has taken a very short view of her tautological work. Having read her carefully this reviewer has decided that she should be rejected as a psychoanalyst, notwithstanding her huge popularity as a feminist. But this reviewer through a nuanced critique of theoretical psychoanalysis find her and her ilk  lacking caritas.",
                    "additional_descriptions": [
                        {
                            "description": "This reviewer had read Kristeva in October, 2016 in this Journal (and the review is freely available online and had garnered some small publicity). Over the last one year this reviewer has taken a very short view of her tautological work. Having read her carefully this reviewer has decided that she should be rejected as a psychoanalyst, notwithstanding her huge popularity as a feminist. But this reviewer through a nuanced critique of theoretical psychoanalysis find her and her ilk lacking caritas.",
                            "type": {
                                "id": "other",
                                "title": {"de": "Sonstige", "en": "Other"},
                            },
                        }
                    ],
                },
                "custom_fields": {
                    "kcr:commons_domain": "hcommons.org",
                    "kcr:submitter_email": "cshubho@gmail.com",
                    "kcr:submitter_username": "subhasis",
                    "kcr:user_defined_tags": [
                        "Anti-psychiatry",
                        "Jacques Lacan",
                        "Julia Kristeva",
                        "psychoanalysis",
                        "theory",
                    ],
                    "hclegacy:collection": "hccollection:1",
                    "hclegacy:file_location": "/srv/www/commons/current/web/app/uploads/humcore/2017/10/o_1brjh02ab14ut1erg1sa4141ioaq7.pdf.julia-kristeva-review.pdf",
                    "hclegacy:file_pid": "hc:15828",
                    "hclegacy:previously_published": "published",
                    "hclegacy:record_change_date": "2023-04-27T20:10:22Z",
                    "hclegacy:record_creation_date": "2017-10-04T11:15:42Z",
                    "hclegacy:submitter_org_memberships": ["hc"],
                    "hclegacy:submitter_id": "1053266",
                },
                "access": {
                    "record": "public",
                    "files": "public",
                    "embargo": {"active": false, "reason": null},
                    "status": "open",
                },
                "files": {
                    "enabled": true,
                    "order": [],
                    "count": 1,
                    "total_bytes": 461930,
                    "entries": {
                        "julia-kristeva-review.pdf": {
                            "ext": "pdf",
                            "key": "julia-kristeva-review.pdf",
                            "metadata": {},
                            "mimetype": "application/pdf",
                            "size": 461930,
                        }
                    },
                },
                "status": "published",
                "stats": {
                    "this_version": {
                        "views": 0,
                        "unique_views": 0,
                        "downloads": 0,
                        "unique_downloads": 0,
                        "data_volume": 0.0,
                    },
                    "all_versions": {
                        "views": 0,
                        "unique_views": 0,
                        "downloads": 0,
                        "unique_downloads": 0,
                        "data_volume": 0.0,
                    },
                },
            },
            {
                "id": "v9zw2-ahb95",
                "created": "2024-02-02T18:41:00.762126+00:00",
                "updated": "2024-02-02T18:41:00.893072+00:00",
                "links": {
                    "self": "https://invenio-dev.hcommons-staging.org/api/records/v9zw2-ahb95",
                    "self_html": "https://invenio-dev.hcommons-staging.org/records/v9zw2-ahb95",
                    "self_doi": "https://invenio-dev.hcommons-staging.org/doi/10.17613/M6BB7B",
                    "doi": "https://handle.stage.datacite.org/10.17613/M6BB7B",
                    "self_iiif_manifest": "https://invenio-dev.hcommons-staging.org/api/iiif/record:v9zw2-ahb95/manifest",
                    "self_iiif_sequence": "https://invenio-dev.hcommons-staging.org/api/iiif/record:v9zw2-ahb95/sequence/default",
                    "files": "https://invenio-dev.hcommons-staging.org/api/records/v9zw2-ahb95/files",
                    "archive": "https://invenio-dev.hcommons-staging.org/api/records/v9zw2-ahb95/files-archive",
                    "latest": "https://invenio-dev.hcommons-staging.org/api/records/v9zw2-ahb95/versions/latest",
                    "latest_html": "https://invenio-dev.hcommons-staging.org/records/v9zw2-ahb95/latest",
                    "draft": "https://invenio-dev.hcommons-staging.org/api/records/v9zw2-ahb95/draft",
                    "versions": "https://invenio-dev.hcommons-staging.org/api/records/v9zw2-ahb95/versions",
                    "access_links": "https://invenio-dev.hcommons-staging.org/api/records/v9zw2-ahb95/access/links",
                    "reserve_doi": "https://invenio-dev.hcommons-staging.org/api/records/v9zw2-ahb95/draft/pids/doi",
                    "communities": "https://invenio-dev.hcommons-staging.org/api/records/v9zw2-ahb95/communities",
                    "communities-suggestions": "https://invenio-dev.hcommons-staging.org/api/records/v9zw2-ahb95/communities-suggestions",
                    "requests": "https://invenio-dev.hcommons-staging.org/api/records/v9zw2-ahb95/requests",
                },
                "revision_id": 3,
                "parent": {
                    "id": "2pqfq-mth02",
                    "communities": {
                        "ids": ["6060e26c-54e3-4f33-8710-1bb89d3672ea"],
                        "default": "6060e26c-54e3-4f33-8710-1bb89d3672ea",
                    },
                },
                "versions": {"is_latest": true, "index": 1},
                "is_published": true,
                "is_draft": false,
                "pids": {
                    "doi": {
                        "identifier": "10.17613/M6BB7B",
                        "provider": "datacite",
                        "client": "datacite",
                    },
                    "oai": {
                        "identifier": "oai:invenio-dev.hcommons-staging.org:v9zw2-ahb95",
                        "provider": "oai",
                    },
                },
                "metadata": {
                    "resource_type": {
                        "id": "textDocument-thesis",
                        "title": {
                            "de": "Abschlussarbeit",
                            "en": "Thesis or dissertation",
                        },
                    },
                    "creators": [
                        {
                            "person_or_org": {
                                "type": "personal",
                                "name": "Lee, Deborah",
                                "given_name": "Deborah",
                                "family_name": "Lee",
                                "identifiers": [
                                    {
                                        "identifier": "poulencing",
                                        "scheme": "hc_username",
                                    }
                                ],
                            },
                            "role": {"id": "author", "title": {"en": "Author"}},
                        }
                    ],
                    "title": "Modelling music: a theoretical approach to the classification of notated Western art music",
                    "publisher": "unknown",
                    "publication_date": "2017",
                    "subjects": [
                        {
                            "id": "http://id.worldcat.org/fast/997916",
                            "subject": "Library science",
                            "scheme": "FAST-topical",
                        },
                        {
                            "id": "http://id.worldcat.org/fast/1030269",
                            "subject": "Music",
                            "scheme": "FAST-topical",
                        },
                    ],
                    "languages": [{"id": "eng", "title": {"en": "English"}}],
                    "identifiers": [
                        {"identifier": "hc:14863", "scheme": "hclegacy-pid"},
                        {"identifier": "1000360-7049", "scheme": "hclegacy-record-id"},
                        {"identifier": "10.17613/M6BB7B", "scheme": "datacite-doi"},
                        {
                            "identifier": "https://doi.org/10.17613/M6BB7B",
                            "scheme": "url",
                        },
                    ],
                    "rights": [
                        {
                            "id": "arr",
                            "title": {"en": "All Rights Reserved"},
                            "description": {
                                "en": "Proprietary material. No permissions are granted for any kind of copyring or re-use. All rights reserved"
                            },
                            "icon": "copyright",
                            "props": {
                                "url": "https://en.wikipedia.org/wiki/All_rights_reserved"
                            },
                        }
                    ],
                    "description": "The classification of notated Western art music is a perennial issue. This thesis analyses and models the knowledge organization of notated Western art music in order to elucidate a theoretical understanding of these classification issues and to offer new ways of viewing music classification in the future. It also offers a domain-based study of music classification, by comparing LIS and music domain classifications of music phenomena throughout the thesis, which culminates in a new model for delineating types of relationships between domain and LIS classifications.  Furthermore, in the process of analysing music classification, the thesis originates a number of novel classification analysis methodologies and innovative classification structures which contribute to the general development of knowledge organization. These include the multiplane approach, reception-infused analysis, webs of Wirkungs (connections) between classification schemes, stress-testing, simultaneous systems of classification and dynamic relationships between facets.\n\nAfter unpicking the major facets of music, subsequent chapters explore the binary vocal/instrumental categorisation, complex mediums including accompaniment and arrangements, the classification of musical instruments, the classification of musical forms and genres, and the quasi-facet of function.  The thesis culminates in five models which illuminate why music is so difficult to classify, as well as presenting novel solutions showing how music classification could be structured in the future.",
                    "additional_descriptions": [
                        {
                            "description": "The classification of notated Western art music is a perennial issue. This thesis analyses and models the knowledge organization of notated Western art music in order to elucidate a theoretical understanding of these classification issues and to offer new ways of viewing music classification in the future. It also offers a domain-based study of music classification, by comparing LIS and music domain classifications of music phenomena throughout the thesis, which culminates in a new model for delineating types of relationships between domain and LIS classifications.  Furthermore, in the process of analysing music classification, the thesis originates a number of novel classification analysis methodologies and innovative classification structures which contribute to the general development of knowledge organization. These include the multiplane approach, reception-infused analysis, webs of Wirkungs (connections) between classification schemes, stress-testing, simultaneous systems of classification and dynamic relationships between facets.\n\nAfter unpicking the major facets of music, subsequent chapters explore the binary vocal/instrumental categorisation, complex mediums including accompaniment and arrangements, the classification of musical instruments, the classification of musical forms and genres, and the quasi-facet of function.  The thesis culminates in five models which illuminate why music is so difficult to classify, as well as presenting novel solutions showing how music classification could be structured in the future.",
                            "type": {
                                "id": "other",
                                "title": {"de": "Sonstige", "en": "Other"},
                            },
                        }
                    ],
                },
                "custom_fields": {
                    "kcr:commons_domain": "hcommons.org",
                    "kcr:sponsoring_institution": "City, University of London",
                    "kcr:submitter_email": "deborah.lee.1@city.ac.uk",
                    "kcr:submitter_username": "poulencing",
                    "kcr:notes": "Unpublished doctoral thesis, awarded in May 2017, Department of Library and Information Science, City, University of London",
                    "kcr:user_defined_tags": [
                        "#CityLis",
                        "#classification",
                        "#knowledgeorganization",
                        "#musicclassification",
                    ],
                    "hclegacy:collection": "hccollection:1",
                    "hclegacy:file_location": "/srv/www/commons/current/web/app/uploads/humcore/2017/07/o_1bltv5q48gu6gdv1t209m91n9b7.pdf.deborah-lee-phd-thesis.pdf",
                    "hclegacy:file_pid": "hc:14864",
                    "hclegacy:previously_published": "not-published",
                    "hclegacy:record_change_date": "2017-07-25T22:59:02Z",
                    "hclegacy:record_creation_date": "2017-07-25T22:59:02Z",
                    "hclegacy:submitter_org_memberships": ["hc"],
                    "hclegacy:submitter_id": "1009532",
                    "hclegacy:groups_for_deposit": [
                        {"group_name": "CityLIS", "group_identifier": "1000734"}
                    ],
                },
                "access": {
                    "record": "public",
                    "files": "public",
                    "embargo": {"active": false, "reason": null},
                    "status": "open",
                },
                "files": {
                    "enabled": true,
                    "order": [],
                    "count": 1,
                    "total_bytes": 4988156,
                    "entries": {
                        "deborah-lee-phd-thesis.pdf": {
                            "ext": "pdf",
                            "key": "deborah-lee-phd-thesis.pdf",
                            "metadata": {},
                            "mimetype": "application/pdf",
                            "size": 4988156,
                        }
                    },
                },
                "status": "published",
                "stats": {
                    "this_version": {
                        "views": 0,
                        "unique_views": 0,
                        "downloads": 0,
                        "unique_downloads": 0,
                        "data_volume": 0.0,
                    },
                    "all_versions": {
                        "views": 0,
                        "unique_views": 0,
                        "downloads": 0,
                        "unique_downloads": 0,
                        "data_volume": 0.0,
                    },
                },
            },
            {
                "id": "fqgb5-t5194",
                "created": "2024-02-02T18:39:39.832892+00:00",
                "updated": "2024-02-02T18:39:39.947439+00:00",
                "links": {
                    "self": "https://invenio-dev.hcommons-staging.org/api/records/fqgb5-t5194",
                    "self_html": "https://invenio-dev.hcommons-staging.org/records/fqgb5-t5194",
                    "self_doi": "https://invenio-dev.hcommons-staging.org/doi/10.17613/M6ZT4M",
                    "doi": "https://handle.stage.datacite.org/10.17613/M6ZT4M",
                    "self_iiif_manifest": "https://invenio-dev.hcommons-staging.org/api/iiif/record:fqgb5-t5194/manifest",
                    "self_iiif_sequence": "https://invenio-dev.hcommons-staging.org/api/iiif/record:fqgb5-t5194/sequence/default",
                    "files": "https://invenio-dev.hcommons-staging.org/api/records/fqgb5-t5194/files",
                    "archive": "https://invenio-dev.hcommons-staging.org/api/records/fqgb5-t5194/files-archive",
                    "latest": "https://invenio-dev.hcommons-staging.org/api/records/fqgb5-t5194/versions/latest",
                    "latest_html": "https://invenio-dev.hcommons-staging.org/records/fqgb5-t5194/latest",
                    "draft": "https://invenio-dev.hcommons-staging.org/api/records/fqgb5-t5194/draft",
                    "versions": "https://invenio-dev.hcommons-staging.org/api/records/fqgb5-t5194/versions",
                    "access_links": "https://invenio-dev.hcommons-staging.org/api/records/fqgb5-t5194/access/links",
                    "reserve_doi": "https://invenio-dev.hcommons-staging.org/api/records/fqgb5-t5194/draft/pids/doi",
                    "communities": "https://invenio-dev.hcommons-staging.org/api/records/fqgb5-t5194/communities",
                    "communities-suggestions": "https://invenio-dev.hcommons-staging.org/api/records/fqgb5-t5194/communities-suggestions",
                    "requests": "https://invenio-dev.hcommons-staging.org/api/records/fqgb5-t5194/requests",
                },
                "revision_id": 3,
                "parent": {
                    "id": "9jfnj-a5h56",
                    "communities": {
                        "ids": ["6060e26c-54e3-4f33-8710-1bb89d3672ea"],
                        "default": "6060e26c-54e3-4f33-8710-1bb89d3672ea",
                    },
                },
                "versions": {"is_latest": true, "index": 1},
                "is_published": true,
                "is_draft": false,
                "pids": {
                    "doi": {
                        "identifier": "10.17613/M6ZT4M",
                        "provider": "datacite",
                        "client": "datacite",
                    },
                    "oai": {
                        "identifier": "oai:invenio-dev.hcommons-staging.org:fqgb5-t5194",
                        "provider": "oai",
                    },
                },
                "metadata": {
                    "resource_type": {
                        "id": "instructionalResource-other",
                        "title": {
                            "de": "Sonstige Lehrmittel",
                            "en": "Other instructional resource",
                        },
                    },
                    "creators": [
                        {
                            "person_or_org": {
                                "type": "personal",
                                "name": "Henriques, Luís",
                                "given_name": "Luís",
                                "family_name": "Henriques",
                                "identifiers": [
                                    {
                                        "identifier": "luiscfhenriques",
                                        "scheme": "hc_username",
                                    }
                                ],
                            },
                            "role": {"id": "author", "title": {"en": "Author"}},
                        }
                    ],
                    "title": "Diego Pisador: Pavana muy llana para tañer",
                    "publisher": "unknown",
                    "publication_date": "2014",
                    "subjects": [
                        {
                            "id": "http://id.worldcat.org/fast/1030893",
                            "subject": "Musicology",
                            "scheme": "FAST-topical",
                        }
                    ],
                    "identifiers": [
                        {"identifier": "hc:14419", "scheme": "hclegacy-pid"},
                        {"identifier": "1000360-6211", "scheme": "hclegacy-record-id"},
                        {"identifier": "10.17613/M6ZT4M", "scheme": "datacite-doi"},
                        {
                            "identifier": "https://doi.org/10.17613/M6ZT4M",
                            "scheme": "url",
                        },
                    ],
                    "rights": [
                        {
                            "id": "arr",
                            "title": {"en": "All Rights Reserved"},
                            "description": {
                                "en": "Proprietary material. No permissions are granted for any kind of copyring or re-use. All rights reserved"
                            },
                            "icon": "copyright",
                            "props": {
                                "url": "https://en.wikipedia.org/wiki/All_rights_reserved"
                            },
                        }
                    ],
                    "description": 'Itabulation of Spanish vihuelist Diego Pisador\'s (c.1450-1521) "Pavana muy llana para tañer" from his Libro de música de vihuela (Salamanca, 1552).',
                },
                "custom_fields": {
                    "kcr:commons_domain": "hcommons.org",
                    "kcr:submitter_email": "luiscfhenriques@gmail.com",
                    "kcr:submitter_username": "luiscfhenriques",
                    "kcr:user_defined_tags": [
                        "16th Century",
                        "Instrumental Music",
                        "Tablature",
                        "Vihuela",
                        "Pavane",
                    ],
                    "hclegacy:collection": "hccollection:1",
                    "hclegacy:file_location": "/srv/www/commons/current/web/app/uploads/humcore/2017/06/o_1biispidm1sstm2i1c61136s1nnp7.mp4.pisador_pavana_muy_llana.mp4",
                    "hclegacy:file_pid": "hc:14420",
                    "hclegacy:previously_published": "published",
                    "hclegacy:record_change_date": "2017-06-14T08:55:50Z",
                    "hclegacy:record_creation_date": "2017-06-14T08:55:50Z",
                    "hclegacy:submitter_org_memberships": ["hc"],
                    "hclegacy:submitter_id": "1009030",
                },
                "access": {
                    "record": "public",
                    "files": "public",
                    "embargo": {"active": false, "reason": null},
                    "status": "open",
                },
                "files": {
                    "enabled": true,
                    "order": [],
                    "count": 1,
                    "total_bytes": 3768382,
                    "entries": {
                        "pisador_pavana_muy_llana.mp4": {
                            "ext": "mp4",
                            "key": "pisador_pavana_muy_llana.mp4",
                            "metadata": {},
                            "mimetype": "video/mp4",
                            "size": 3768382,
                        }
                    },
                },
                "status": "published",
                "stats": {
                    "this_version": {
                        "views": 0,
                        "unique_views": 0,
                        "downloads": 0,
                        "unique_downloads": 0,
                        "data_volume": 0.0,
                    },
                    "all_versions": {
                        "views": 0,
                        "unique_views": 0,
                        "downloads": 0,
                        "unique_downloads": 0,
                        "data_volume": 0.0,
                    },
                },
            },
            {
                "id": "ytza2-t3e03",
                "created": "2024-02-02T18:39:17.333124+00:00",
                "updated": "2024-02-02T18:39:17.449865+00:00",
                "links": {
                    "self": "https://invenio-dev.hcommons-staging.org/api/records/ytza2-t3e03",
                    "self_html": "https://invenio-dev.hcommons-staging.org/records/ytza2-t3e03",
                    "self_doi": "https://invenio-dev.hcommons-staging.org/doi/10.17613/M65T2Q",
                    "doi": "https://handle.stage.datacite.org/10.17613/M65T2Q",
                    "self_iiif_manifest": "https://invenio-dev.hcommons-staging.org/api/iiif/record:ytza2-t3e03/manifest",
                    "self_iiif_sequence": "https://invenio-dev.hcommons-staging.org/api/iiif/record:ytza2-t3e03/sequence/default",
                    "files": "https://invenio-dev.hcommons-staging.org/api/records/ytza2-t3e03/files",
                    "archive": "https://invenio-dev.hcommons-staging.org/api/records/ytza2-t3e03/files-archive",
                    "latest": "https://invenio-dev.hcommons-staging.org/api/records/ytza2-t3e03/versions/latest",
                    "latest_html": "https://invenio-dev.hcommons-staging.org/records/ytza2-t3e03/latest",
                    "draft": "https://invenio-dev.hcommons-staging.org/api/records/ytza2-t3e03/draft",
                    "versions": "https://invenio-dev.hcommons-staging.org/api/records/ytza2-t3e03/versions",
                    "access_links": "https://invenio-dev.hcommons-staging.org/api/records/ytza2-t3e03/access/links",
                    "reserve_doi": "https://invenio-dev.hcommons-staging.org/api/records/ytza2-t3e03/draft/pids/doi",
                    "communities": "https://invenio-dev.hcommons-staging.org/api/records/ytza2-t3e03/communities",
                    "communities-suggestions": "https://invenio-dev.hcommons-staging.org/api/records/ytza2-t3e03/communities-suggestions",
                    "requests": "https://invenio-dev.hcommons-staging.org/api/records/ytza2-t3e03/requests",
                },
                "revision_id": 3,
                "parent": {
                    "id": "pz8gd-ncz69",
                    "communities": {
                        "ids": ["6060e26c-54e3-4f33-8710-1bb89d3672ea"],
                        "default": "6060e26c-54e3-4f33-8710-1bb89d3672ea",
                    },
                },
                "versions": {"is_latest": true, "index": 1},
                "is_published": true,
                "is_draft": false,
                "pids": {
                    "doi": {
                        "identifier": "10.17613/M65T2Q",
                        "provider": "datacite",
                        "client": "datacite",
                    },
                    "oai": {
                        "identifier": "oai:invenio-dev.hcommons-staging.org:ytza2-t3e03",
                        "provider": "oai",
                    },
                },
                "metadata": {
                    "resource_type": {
                        "id": "audiovisual-musicalRecording",
                        "title": {"de": "Musikaufnahmen", "en": "Musical recording"},
                    },
                    "creators": [
                        {
                            "person_or_org": {
                                "type": "personal",
                                "name": "Henriques, Luís",
                                "given_name": "Luís",
                                "family_name": "Henriques",
                                "identifiers": [
                                    {
                                        "identifier": "luiscfhenriques",
                                        "scheme": "hc_username",
                                    }
                                ],
                            },
                            "role": {"id": "author", "title": {"en": "Author"}},
                        }
                    ],
                    "title": "Dominica Resurrectionis: Victimae Paschali laudes",
                    "publisher": "unknown",
                    "publication_date": "2014",
                    "subjects": [
                        {
                            "id": "http://id.worldcat.org/fast/1030893",
                            "subject": "Musicology",
                            "scheme": "FAST-topical",
                        }
                    ],
                    "languages": [{"id": "eng", "title": {"en": "English"}}],
                    "identifiers": [
                        {"identifier": "hc:14279", "scheme": "hclegacy-pid"},
                        {"identifier": "1000360-6059", "scheme": "hclegacy-record-id"},
                        {"identifier": "10.17613/M65T2Q", "scheme": "datacite-doi"},
                        {
                            "identifier": "https://doi.org/10.17613/M65T2Q",
                            "scheme": "url",
                        },
                    ],
                    "rights": [
                        {
                            "id": "arr",
                            "title": {"en": "All Rights Reserved"},
                            "description": {
                                "en": "Proprietary material. No permissions are granted for any kind of copyring or re-use. All rights reserved"
                            },
                            "icon": "copyright",
                            "props": {
                                "url": "https://en.wikipedia.org/wiki/All_rights_reserved"
                            },
                        }
                    ],
                    "description": 'Sequence for the Sunday of Resurrection (Easter Sunday) "Victimae Paschali laudes" from the eighteenth-century choirbook P-AHc MM 414 preserved in the music archive of the Capitular Archive of Angra Cathedral (Terceira, Azores).',
                },
                "custom_fields": {
                    "kcr:commons_domain": "hcommons.org",
                    "kcr:submitter_email": "luiscfhenriques@gmail.com",
                    "kcr:submitter_username": "luiscfhenriques",
                    "kcr:user_defined_tags": [
                        "18th Century",
                        "Angra Cathedral",
                        "Choirbook",
                        "Plainchant",
                        "Sequence",
                    ],
                    "hclegacy:collection": "hccollection:1",
                    "hclegacy:file_location": "/srv/www/commons/current/web/app/uploads/humcore/2017/06/o_1bi4jsb2n1csj18cv1hbiai91p6f7.mp4.victimae_paschali_laudes.mp4",
                    "hclegacy:file_pid": "hc:14280",
                    "hclegacy:previously_published": "published",
                    "hclegacy:record_change_date": "2017-06-08T19:51:40Z",
                    "hclegacy:record_creation_date": "2017-06-08T19:51:40Z",
                    "hclegacy:submitter_org_memberships": ["hc"],
                    "hclegacy:submitter_id": "1009030",
                },
                "access": {
                    "record": "public",
                    "files": "public",
                    "embargo": {"active": false, "reason": null},
                    "status": "open",
                },
                "files": {
                    "enabled": true,
                    "order": [],
                    "count": 1,
                    "total_bytes": 9286045,
                    "entries": {
                        "victimae_paschali_laudes.mp4": {
                            "ext": "mp4",
                            "key": "victimae_paschali_laudes.mp4",
                            "metadata": {},
                            "mimetype": "video/mp4",
                            "size": 9286045,
                        }
                    },
                },
                "status": "published",
                "stats": {
                    "this_version": {
                        "views": 0,
                        "unique_views": 0,
                        "downloads": 0,
                        "unique_downloads": 0,
                        "data_volume": 0.0,
                    },
                    "all_versions": {
                        "views": 0,
                        "unique_views": 0,
                        "downloads": 0,
                        "unique_downloads": 0,
                        "data_volume": 0.0,
                    },
                },
            },
            {
                "id": "695c2-f7f60",
                "created": "2024-02-02T18:36:20.598030+00:00",
                "updated": "2024-02-02T18:36:20.739248+00:00",
                "links": {
                    "self": "https://invenio-dev.hcommons-staging.org/api/records/695c2-f7f60",
                    "self_html": "https://invenio-dev.hcommons-staging.org/records/695c2-f7f60",
                    "self_doi": "https://invenio-dev.hcommons-staging.org/doi/10.17613/M6P08C",
                    "doi": "https://handle.stage.datacite.org/10.17613/M6P08C",
                    "self_iiif_manifest": "https://invenio-dev.hcommons-staging.org/api/iiif/record:695c2-f7f60/manifest",
                    "self_iiif_sequence": "https://invenio-dev.hcommons-staging.org/api/iiif/record:695c2-f7f60/sequence/default",
                    "files": "https://invenio-dev.hcommons-staging.org/api/records/695c2-f7f60/files",
                    "archive": "https://invenio-dev.hcommons-staging.org/api/records/695c2-f7f60/files-archive",
                    "latest": "https://invenio-dev.hcommons-staging.org/api/records/695c2-f7f60/versions/latest",
                    "latest_html": "https://invenio-dev.hcommons-staging.org/records/695c2-f7f60/latest",
                    "draft": "https://invenio-dev.hcommons-staging.org/api/records/695c2-f7f60/draft",
                    "versions": "https://invenio-dev.hcommons-staging.org/api/records/695c2-f7f60/versions",
                    "access_links": "https://invenio-dev.hcommons-staging.org/api/records/695c2-f7f60/access/links",
                    "reserve_doi": "https://invenio-dev.hcommons-staging.org/api/records/695c2-f7f60/draft/pids/doi",
                    "communities": "https://invenio-dev.hcommons-staging.org/api/records/695c2-f7f60/communities",
                    "communities-suggestions": "https://invenio-dev.hcommons-staging.org/api/records/695c2-f7f60/communities-suggestions",
                    "requests": "https://invenio-dev.hcommons-staging.org/api/records/695c2-f7f60/requests",
                },
                "revision_id": 3,
                "parent": {
                    "id": "yea92-08298",
                    "communities": {
                        "ids": ["6060e26c-54e3-4f33-8710-1bb89d3672ea"],
                        "default": "6060e26c-54e3-4f33-8710-1bb89d3672ea",
                    },
                },
                "versions": {"is_latest": true, "index": 1},
                "is_published": true,
                "is_draft": false,
                "pids": {
                    "doi": {
                        "identifier": "10.17613/M6P08C",
                        "provider": "datacite",
                        "client": "datacite",
                    },
                    "oai": {
                        "identifier": "oai:invenio-dev.hcommons-staging.org:695c2-f7f60",
                        "provider": "oai",
                    },
                },
                "metadata": {
                    "resource_type": {
                        "id": "textDocument-journalArticle",
                        "title": {
                            "de": "Zeitschriftenartikel",
                            "en": "Journal article",
                        },
                    },
                    "creators": [
                        {
                            "person_or_org": {
                                "type": "personal",
                                "name": "Fradejas Rueda, José Manuel",
                                "given_name": "José Manuel",
                                "family_name": "Fradejas Rueda",
                                "identifiers": [
                                    {"identifier": "fradejas", "scheme": "hc_username"}
                                ],
                            },
                            "role": {"id": "author", "title": {"en": "Author"}},
                        }
                    ],
                    "title": "Iluminar la caza en la edad media: aproximación a la iconografía venatoria medieval iberorrománica",
                    "publisher": "Universidad de Alcalá",
                    "publication_date": "2016",
                    "subjects": [
                        {
                            "id": "http://id.worldcat.org/fast/967235",
                            "subject": "Illumination of books and manuscripts",
                            "scheme": "FAST-topical",
                        },
                        {
                            "id": "http://id.worldcat.org/fast/1128568",
                            "subject": "Spanish literature",
                            "scheme": "FAST-topical",
                        },
                    ],
                    "languages": [{"id": "spa", "title": {"en": "Spanish"}}],
                    "identifiers": [
                        {"identifier": "hc:13139", "scheme": "hclegacy-pid"},
                        {"identifier": "1000360-4773", "scheme": "hclegacy-record-id"},
                        {"identifier": "10.17613/M6P08C", "scheme": "datacite-doi"},
                        {
                            "identifier": "https://doi.org/10.17613/M6P08C",
                            "scheme": "url",
                        },
                    ],
                    "rights": [
                        {
                            "id": "cc-by-nc-nd-4.0",
                            "title": {
                                "en": "Creative Commons Attribution Non Commercial No Derivatives 4.0 International"
                            },
                            "description": {"en": ""},
                            "icon": "cc-by-nc-nd-icon",
                            "props": {
                                "url": "https://creativecommons.org/licenses/by-nc-nd/4.0/legalcode",
                                "scheme": "spdx",
                            },
                        }
                    ],
                    "description": "Desde el arte rupestre la caza ha sido uno de los temas predilectos. Duran- te la Edad Media surgen los libros de caza, aunque tienen un tenue antecedente en la antigüedad greco-latina, una literatura técnica y práctica que en su momento de apogeo desarrolla un interesante esquema iluminador. Aunque la península Ibérica que presenta una literatura venatoria muy característica llena de notas personales y aspectos exclusivos como la geografía de la caza, sin embargo es paupérrima a la hora de ilustrar los textos puesto que básicamente es una literatura técnica que se li- mita a presentar los instrumentos necesarios, no obstante hay algunos ejemplos muy interesantes, aunque las mejores imágenes de la caza no ilustran los libros técnicos sino otro tipos literarios. Tras una visión de la historia de la representación de la caza y de los libros de caza ilustrados, se analizan las miniaturas del Libro de la montería y se establece cuál es el significado y función de cada una de ellas. Posteriormente se estudian los instrumentos médico-quirúrgicos mostrados en los libros de cetrería, especialmente en la serie iniciada por el Livro da falcoaria de Pero Menino y difun- dida por el Libro de la caza de las aves de López de Ayala. Se cierra con un análisis de las miniaturas venatorias de las Cantigas de Santa María.",
                },
                "custom_fields": {
                    "journal:journal": {
                        "title": "Revista de Poética Medieval",
                        "volume": "30",
                        "pages": "105-130",
                        "issn": "1137-8905",
                    },
                    "kcr:commons_domain": "hcommons.org",
                    "kcr:submitter_email": "jose.fradejas.rueda@gmail.com",
                    "kcr:submitter_username": "fradejas",
                    "kcr:user_defined_tags": [
                        "Hunting",
                        "Falconry",
                        "Illuminated manuscripts",
                        "Medieval studies",
                    ],
                    "hclegacy:collection": "hccollection:1",
                    "hclegacy:file_location": "/srv/www/commons/current/web/app/uploads/humcore/2017/05/o_1bfbl1qi5j1rbas10bp9ig78l7.pdf.iluminar_la_caza_en_la_edad_media_aproxi.pdf",
                    "hclegacy:file_pid": "hc:13140",
                    "hclegacy:previously_published": "published",
                    "hclegacy:record_change_date": "2017-05-05T06:36:07Z",
                    "hclegacy:record_creation_date": "2017-05-05T06:36:07Z",
                    "hclegacy:submitter_org_memberships": ["hc"],
                    "hclegacy:submitter_id": "1008647",
                },
                "access": {
                    "record": "public",
                    "files": "public",
                    "embargo": {"active": false, "reason": null},
                    "status": "open",
                },
                "files": {
                    "enabled": true,
                    "order": [],
                    "count": 1,
                    "total_bytes": 1597343,
                    "entries": {
                        "iluminar_la_caza_en_la_edad_media_aproxi.pdf": {
                            "ext": "pdf",
                            "key": "iluminar_la_caza_en_la_edad_media_aproxi.pdf",
                            "metadata": {},
                            "mimetype": "application/pdf",
                            "size": 1597343,
                        }
                    },
                },
                "status": "published",
                "stats": {
                    "this_version": {
                        "views": 0,
                        "unique_views": 0,
                        "downloads": 0,
                        "unique_downloads": 0,
                        "data_volume": 0.0,
                    },
                    "all_versions": {
                        "views": 0,
                        "unique_views": 0,
                        "downloads": 0,
                        "unique_downloads": 0,
                        "data_volume": 0.0,
                    },
                },
            },
            {
                "id": "b88er-dr328",
                "created": "2024-02-02T18:35:17.234838+00:00",
                "updated": "2024-02-02T18:35:17.359173+00:00",
                "links": {
                    "self": "https://invenio-dev.hcommons-staging.org/api/records/b88er-dr328",
                    "self_html": "https://invenio-dev.hcommons-staging.org/records/b88er-dr328",
                    "self_doi": "https://invenio-dev.hcommons-staging.org/doi/10.17613/M6TM15",
                    "doi": "https://handle.stage.datacite.org/10.17613/M6TM15",
                    "self_iiif_manifest": "https://invenio-dev.hcommons-staging.org/api/iiif/record:b88er-dr328/manifest",
                    "self_iiif_sequence": "https://invenio-dev.hcommons-staging.org/api/iiif/record:b88er-dr328/sequence/default",
                    "files": "https://invenio-dev.hcommons-staging.org/api/records/b88er-dr328/files",
                    "archive": "https://invenio-dev.hcommons-staging.org/api/records/b88er-dr328/files-archive",
                    "latest": "https://invenio-dev.hcommons-staging.org/api/records/b88er-dr328/versions/latest",
                    "latest_html": "https://invenio-dev.hcommons-staging.org/records/b88er-dr328/latest",
                    "draft": "https://invenio-dev.hcommons-staging.org/api/records/b88er-dr328/draft",
                    "versions": "https://invenio-dev.hcommons-staging.org/api/records/b88er-dr328/versions",
                    "access_links": "https://invenio-dev.hcommons-staging.org/api/records/b88er-dr328/access/links",
                    "reserve_doi": "https://invenio-dev.hcommons-staging.org/api/records/b88er-dr328/draft/pids/doi",
                    "communities": "https://invenio-dev.hcommons-staging.org/api/records/b88er-dr328/communities",
                    "communities-suggestions": "https://invenio-dev.hcommons-staging.org/api/records/b88er-dr328/communities-suggestions",
                    "requests": "https://invenio-dev.hcommons-staging.org/api/records/b88er-dr328/requests",
                },
                "revision_id": 3,
                "parent": {
                    "id": "xvvza-68k27",
                    "communities": {
                        "ids": ["6060e26c-54e3-4f33-8710-1bb89d3672ea"],
                        "default": "6060e26c-54e3-4f33-8710-1bb89d3672ea",
                    },
                },
                "versions": {"is_latest": true, "index": 1},
                "is_published": true,
                "is_draft": false,
                "pids": {
                    "doi": {
                        "identifier": "10.17613/M6TM15",
                        "provider": "datacite",
                        "client": "datacite",
                    },
                    "oai": {
                        "identifier": "oai:invenio-dev.hcommons-staging.org:b88er-dr328",
                        "provider": "oai",
                    },
                },
                "metadata": {
                    "resource_type": {
                        "id": "textDocument-journalArticle",
                        "title": {
                            "de": "Zeitschriftenartikel",
                            "en": "Journal article",
                        },
                    },
                    "creators": [
                        {
                            "person_or_org": {
                                "type": "personal",
                                "name": "Borchardt, Francis",
                                "given_name": "Francis",
                                "family_name": "Borchardt",
                                "identifiers": [
                                    {
                                        "identifier": "francisborchardt",
                                        "scheme": "hc_username",
                                    }
                                ],
                            },
                            "role": {"id": "author", "title": {"en": "Author"}},
                        }
                    ],
                    "title": "What Do You Do When a Text is Failing? The Letter of Aristeas and the Need for a New Pentateuch",
                    "publisher": "unknown",
                    "publication_date": "2017",
                    "subjects": [
                        {
                            "id": "http://id.worldcat.org/fast/947441",
                            "subject": "Greek literature",
                            "scheme": "FAST-topical",
                        },
                        {
                            "id": "http://id.worldcat.org/fast/982834",
                            "subject": "Jewish literature",
                            "scheme": "FAST-topical",
                        },
                    ],
                    "languages": [{"id": "eng", "title": {"en": "English"}}],
                    "identifiers": [
                        {"identifier": "hc:12797", "scheme": "hclegacy-pid"},
                        {"identifier": "1000360-4355", "scheme": "hclegacy-record-id"},
                        {"identifier": "10.17613/M6TM15", "scheme": "datacite-doi"},
                        {
                            "identifier": "https://doi.org/10.17613/M6TM15",
                            "scheme": "url",
                        },
                    ],
                    "rights": [
                        {
                            "id": "arr",
                            "title": {"en": "All Rights Reserved"},
                            "description": {
                                "en": "Proprietary material. No permissions are granted for any kind of copyring or re-use. All rights reserved"
                            },
                            "icon": "copyright",
                            "props": {
                                "url": "https://en.wikipedia.org/wiki/All_rights_reserved"
                            },
                        }
                    ],
                    "description": "This study highlights features of the Letter of Aristeas that reveal how that story conceives of the royal translation project. It will apply the concept of 'auxiliary texts' developed by Markus Dubischar based on the conversation theory of Paul Grice in order to show that Aristeas understands the Hebrew Pentateuch as a failing text. It will be shown that because Aristeas both respects the traditions and teachings contained within the Pentateuch, and recognizes the failure of the text outside of a particular context, it sees the translation as necessary for the Pentateuch's survival. The study will compare the statements related in prologues from Graeco-Roman 'auxiliary texts' to statements in the Letter of Aristeas to underline the ways how the Greek translation of the Hebrew text is simultaneously conceived of as a correction of the problems inherent in the Hebrew text tradition, and is not attempting to entirely replace that tradition.",
                },
                "custom_fields": {
                    "journal:journal": {
                        "title": "Journal for the Study of Judaism",
                        "volume": "48",
                        "pages": "1-21",
                    },
                    "kcr:commons_domain": "hcommons.org",
                    "kcr:submitter_email": "Archaeology@gmail.com",
                    "kcr:submitter_username": "francisborchardt",
                    "kcr:user_defined_tags": ["Ancient literature", "Biblical studies"],
                    "hclegacy:collection": "hccollection:1",
                    "hclegacy:file_location": "/srv/www/commons/current/web/app/uploads/humcore/2017/04/o_1bevgnvi5nic1g261enr1bu017d77.pdf.borchardt-what-do-you-do-when-a-text-is-failing.pdf",
                    "hclegacy:file_pid": "hc:12798",
                    "hclegacy:previously_published": "published",
                    "hclegacy:record_change_date": "2017-05-01T17:40:01Z",
                    "hclegacy:record_creation_date": "2017-04-30T13:28:20Z",
                    "hclegacy:submitter_org_memberships": ["hc"],
                    "hclegacy:submitter_id": "1008648",
                    "hclegacy:groups_for_deposit": [
                        {
                            "group_name": "Ancient Greece & Rome",
                            "group_identifier": "1000636",
                        },
                        {
                            "group_name": "Ancient Near East",
                            "group_identifier": "1000590",
                        },
                        {
                            "group_name": "Biblical Studies",
                            "group_identifier": "1000689",
                        },
                        {"group_name": "Jewish Studies", "group_identifier": "1000737"},
                        {
                            "group_name": "Religious Studies",
                            "group_identifier": "1000641",
                        },
                    ],
                },
                "access": {
                    "record": "public",
                    "files": "public",
                    "embargo": {"active": false, "reason": null},
                    "status": "open",
                },
                "files": {
                    "enabled": true,
                    "order": [],
                    "count": 1,
                    "total_bytes": 546691,
                    "entries": {
                        "borchardt-what-do-you-do-when-a-text-is-failing.pdf": {
                            "ext": "pdf",
                            "key": "borchardt-what-do-you-do-when-a-text-is-failing.pdf",
                            "metadata": {},
                            "mimetype": "application/pdf",
                            "size": 546691,
                        }
                    },
                },
                "status": "published",
                "stats": {
                    "this_version": {
                        "views": 0,
                        "unique_views": 0,
                        "downloads": 0,
                        "unique_downloads": 0,
                        "data_volume": 0.0,
                    },
                    "all_versions": {
                        "views": 0,
                        "unique_views": 0,
                        "downloads": 0,
                        "unique_downloads": 0,
                        "data_volume": 0.0,
                    },
                },
            },
            {
                "id": "7team-04t23",
                "created": "2024-02-02T18:34:22.435120+00:00",
                "updated": "2024-02-02T18:34:22.582471+00:00",
                "links": {
                    "self": "https://invenio-dev.hcommons-staging.org/api/records/7team-04t23",
                    "self_html": "https://invenio-dev.hcommons-staging.org/records/7team-04t23",
                    "self_doi": "https://invenio-dev.hcommons-staging.org/doi/10.17613/M6GQ0Q",
                    "doi": "https://handle.stage.datacite.org/10.17613/M6GQ0Q",
                    "self_iiif_manifest": "https://invenio-dev.hcommons-staging.org/api/iiif/record:7team-04t23/manifest",
                    "self_iiif_sequence": "https://invenio-dev.hcommons-staging.org/api/iiif/record:7team-04t23/sequence/default",
                    "files": "https://invenio-dev.hcommons-staging.org/api/records/7team-04t23/files",
                    "archive": "https://invenio-dev.hcommons-staging.org/api/records/7team-04t23/files-archive",
                    "latest": "https://invenio-dev.hcommons-staging.org/api/records/7team-04t23/versions/latest",
                    "latest_html": "https://invenio-dev.hcommons-staging.org/records/7team-04t23/latest",
                    "draft": "https://invenio-dev.hcommons-staging.org/api/records/7team-04t23/draft",
                    "versions": "https://invenio-dev.hcommons-staging.org/api/records/7team-04t23/versions",
                    "access_links": "https://invenio-dev.hcommons-staging.org/api/records/7team-04t23/access/links",
                    "reserve_doi": "https://invenio-dev.hcommons-staging.org/api/records/7team-04t23/draft/pids/doi",
                    "communities": "https://invenio-dev.hcommons-staging.org/api/records/7team-04t23/communities",
                    "communities-suggestions": "https://invenio-dev.hcommons-staging.org/api/records/7team-04t23/communities-suggestions",
                    "requests": "https://invenio-dev.hcommons-staging.org/api/records/7team-04t23/requests",
                },
                "revision_id": 3,
                "parent": {
                    "id": "37d0n-pnt05",
                    "communities": {
                        "ids": ["6060e26c-54e3-4f33-8710-1bb89d3672ea"],
                        "default": "6060e26c-54e3-4f33-8710-1bb89d3672ea",
                    },
                },
                "versions": {"is_latest": true, "index": 1},
                "is_published": true,
                "is_draft": false,
                "pids": {
                    "doi": {
                        "identifier": "10.17613/M6GQ0Q",
                        "provider": "datacite",
                        "client": "datacite",
                    },
                    "oai": {
                        "identifier": "oai:invenio-dev.hcommons-staging.org:7team-04t23",
                        "provider": "oai",
                    },
                },
                "metadata": {
                    "resource_type": {
                        "id": "textDocument-whitePaper",
                        "title": {"de": "weißes Papier", "en": "White paper"},
                    },
                    "creators": [
                        {
                            "person_or_org": {
                                "type": "personal",
                                "name": "Manning, Patrick",
                                "given_name": "Patrick",
                                "family_name": "Manning",
                            },
                            "role": {
                                "id": "projectOrTeamLeader",
                                "title": {
                                    "de": "ProjektleiterIn",
                                    "en": "Project or team leader",
                                },
                            },
                        },
                        {
                            "person_or_org": {
                                "type": "personal",
                                "name": "Manning, Patrick",
                                "given_name": "Patrick",
                                "family_name": "Manning",
                            },
                            "role": {"id": "author", "title": {"en": "Author"}},
                        },
                        {
                            "person_or_org": {
                                "type": "personal",
                                "name": "Mostern, Ruth",
                                "given_name": "Ruth",
                                "family_name": "Mostern",
                            },
                            "role": {
                                "id": "projectOrTeamLeader",
                                "title": {
                                    "de": "ProjektleiterIn",
                                    "en": "Project or team leader",
                                },
                            },
                        },
                        {
                            "person_or_org": {
                                "type": "personal",
                                "name": "Mostern, Ruth",
                                "given_name": "Ruth",
                                "family_name": "Mostern",
                            },
                            "role": {"id": "author", "title": {"en": "Author"}},
                        },
                    ],
                    "title": "World-Historical Gazetteer",
                    "publisher": "unknown",
                    "publication_date": "2015",
                    "subjects": [
                        {
                            "id": "http://id.worldcat.org/fast/940469",
                            "subject": "Geography",
                            "scheme": "FAST-topical",
                        },
                        {
                            "id": "http://id.worldcat.org/fast/1411628",
                            "subject": "History",
                            "scheme": "FAST-form",
                        },
                        {
                            "id": "http://id.worldcat.org/fast/976131",
                            "subject": "Interdisciplinary research",
                            "scheme": "FAST-topical",
                        },
                    ],
                    "dates": [
                        {
                            "date": "2015-11-10",
                            "type": {
                                "id": "issued",
                                "title": {"de": "Veröffentlicht", "en": "Issued"},
                            },
                            "description": "Publication date",
                        }
                    ],
                    "languages": [{"id": "eng", "title": {"en": "English"}}],
                    "identifiers": [
                        {"identifier": "hc:12283", "scheme": "hclegacy-pid"},
                        {"identifier": "1000360-3759", "scheme": "hclegacy-record-id"},
                        {"identifier": "10.17613/M6GQ0Q", "scheme": "datacite-doi"},
                        {
                            "identifier": "https://doi.org/10.17613/M6GQ0Q",
                            "scheme": "url",
                        },
                    ],
                    "rights": [
                        {
                            "id": "cc-by-nc-4.0",
                            "title": {
                                "en": "Creative Commons Attribution Non Commercial 4.0 International"
                            },
                            "description": {"en": ""},
                            "icon": "cc-by-nc-icon",
                            "props": {
                                "url": "https://creativecommons.org/licenses/by-nc/4.0/legalcode",
                                "scheme": "spdx",
                            },
                        }
                    ],
                    "description": "This project will advance work toward creation of a world-historical gazetteer that will provide comprehensive databases of places throughout the world since 1500 CE, including attention to the range of attributes known for each place. To satisfy the needs of all the large-scale historical data resources now being created, there is need for such a comprehensive and general gazetteer system. The convening of a two-day workshop, including leading figures who have developed gazetteers and the datasets in which they are incorporated, will bring about a research design for this world-historical gazetteer system, which can then be implemented in subsequent work. Four small research tasks concerning services, standards, and content will bring immediate advance toward implementation. The project is organized by the Collaborative for Historical Information and Analysis (CHIA), which has a record in sustaining collaborations for large-scale humanities work.",
                },
                "custom_fields": {
                    "kcr:commons_domain": "hcommons.org",
                    "kcr:submitter_email": "hc@hcommons.org",
                    "kcr:submitter_username": "hcadmin",
                    "kcr:notes": "A two-day workshop in Pittsburgh, Pennsylvania, and follow-up activities for geographers, historians, and information scientists to consider how a world-historical gazetteer might be created that combines earlier work in regional and historical place name databases.",
                    "kcr:user_defined_tags": [
                        "NEH White papers",
                        "Digital Humanities Start-Up Grants",
                        "NEH Digital Humanities",
                    ],
                    "hclegacy:collection": "hccollection:1",
                    "hclegacy:file_location": "/srv/www/commons/current/web/app/uploads/humcore/2017/04/NEH_whitepapers.pdf.hd-51828-14.pdf",
                    "hclegacy:file_pid": "hc:12284",
                    "hclegacy:previously_published": "not-published",
                    "hclegacy:record_change_date": "2017-04-17T19:20:00Z",
                    "hclegacy:record_creation_date": "2017-04-17T19:20:00Z",
                    "hclegacy:submitter_org_memberships": ["hc"],
                    "hclegacy:submitter_id": "1006552",
                    "hclegacy:groups_for_deposit": [
                        {"group_name": "Data Rescue", "group_identifier": "1000758"}
                    ],
                },
                "access": {
                    "record": "public",
                    "files": "public",
                    "embargo": {"active": false, "reason": null},
                    "status": "open",
                },
                "files": {
                    "enabled": true,
                    "order": [],
                    "count": 1,
                    "total_bytes": 212499,
                    "entries": {
                        "hd-51828-14.pdf": {
                            "ext": "pdf",
                            "key": "hd-51828-14.pdf",
                            "metadata": {},
                            "mimetype": "application/pdf",
                            "size": 212499,
                        }
                    },
                },
                "status": "published",
                "stats": {
                    "this_version": {
                        "views": 0,
                        "unique_views": 0,
                        "downloads": 0,
                        "unique_downloads": 0,
                        "data_volume": 0.0,
                    },
                    "all_versions": {
                        "views": 0,
                        "unique_views": 0,
                        "downloads": 0,
                        "unique_downloads": 0,
                        "data_volume": 0.0,
                    },
                },
            },
            {
                "id": "abzsy-yqp60",
                "created": "2024-02-02T18:33:35.181698+00:00",
                "updated": "2024-02-02T18:33:35.304122+00:00",
                "links": {
                    "self": "https://invenio-dev.hcommons-staging.org/api/records/abzsy-yqp60",
                    "self_html": "https://invenio-dev.hcommons-staging.org/records/abzsy-yqp60",
                    "self_doi": "https://invenio-dev.hcommons-staging.org/doi/10.17613/M6CH2G",
                    "doi": "https://handle.stage.datacite.org/10.17613/M6CH2G",
                    "self_iiif_manifest": "https://invenio-dev.hcommons-staging.org/api/iiif/record:abzsy-yqp60/manifest",
                    "self_iiif_sequence": "https://invenio-dev.hcommons-staging.org/api/iiif/record:abzsy-yqp60/sequence/default",
                    "files": "https://invenio-dev.hcommons-staging.org/api/records/abzsy-yqp60/files",
                    "archive": "https://invenio-dev.hcommons-staging.org/api/records/abzsy-yqp60/files-archive",
                    "latest": "https://invenio-dev.hcommons-staging.org/api/records/abzsy-yqp60/versions/latest",
                    "latest_html": "https://invenio-dev.hcommons-staging.org/records/abzsy-yqp60/latest",
                    "draft": "https://invenio-dev.hcommons-staging.org/api/records/abzsy-yqp60/draft",
                    "versions": "https://invenio-dev.hcommons-staging.org/api/records/abzsy-yqp60/versions",
                    "access_links": "https://invenio-dev.hcommons-staging.org/api/records/abzsy-yqp60/access/links",
                    "reserve_doi": "https://invenio-dev.hcommons-staging.org/api/records/abzsy-yqp60/draft/pids/doi",
                    "communities": "https://invenio-dev.hcommons-staging.org/api/records/abzsy-yqp60/communities",
                    "communities-suggestions": "https://invenio-dev.hcommons-staging.org/api/records/abzsy-yqp60/communities-suggestions",
                    "requests": "https://invenio-dev.hcommons-staging.org/api/records/abzsy-yqp60/requests",
                },
                "revision_id": 3,
                "parent": {
                    "id": "qy2ye-2ga08",
                    "communities": {
                        "ids": ["6060e26c-54e3-4f33-8710-1bb89d3672ea"],
                        "default": "6060e26c-54e3-4f33-8710-1bb89d3672ea",
                    },
                },
                "versions": {"is_latest": true, "index": 1},
                "is_published": true,
                "is_draft": false,
                "pids": {
                    "doi": {
                        "identifier": "10.17613/M6CH2G",
                        "provider": "datacite",
                        "client": "datacite",
                    },
                    "oai": {
                        "identifier": "oai:invenio-dev.hcommons-staging.org:abzsy-yqp60",
                        "provider": "oai",
                    },
                },
                "metadata": {
                    "resource_type": {
                        "id": "textDocument-bibliography",
                        "title": {"de": "Literaturverzeichnis", "en": "Bibliography"},
                    },
                    "creators": [
                        {
                            "person_or_org": {
                                "type": "personal",
                                "name": "Albertson, Hallqvist",
                                "given_name": "Hallqvist",
                                "family_name": "Albertson",
                                "identifiers": [
                                    {"identifier": "albertson", "scheme": "hc_username"}
                                ],
                            },
                            "role": {"id": "author", "title": {"en": "Author"}},
                        }
                    ],
                    "title": "Cultural Anthropology Background Reading",
                    "publisher": "unknown",
                    "publication_date": "2016",
                    "subjects": [
                        {
                            "id": "http://id.worldcat.org/fast/810196",
                            "subject": "Anthropology",
                            "scheme": "FAST-topical",
                        },
                        {
                            "id": "http://id.worldcat.org/fast/810233",
                            "subject": "Anthropology--Social aspects",
                            "scheme": "FAST-topical",
                        },
                    ],
                    "languages": [{"id": "eng", "title": {"en": "English"}}],
                    "identifiers": [
                        {"identifier": "hc:11781", "scheme": "hclegacy-pid"},
                        {"identifier": "1000360-3197", "scheme": "hclegacy-record-id"},
                        {"identifier": "10.17613/M6CH2G", "scheme": "datacite-doi"},
                        {
                            "identifier": "https://doi.org/10.17613/M6CH2G",
                            "scheme": "url",
                        },
                    ],
                    "rights": [
                        {
                            "id": "cc-by-nc-sa-4.0",
                            "title": {
                                "en": "Creative Commons Attribution Non Commercial Share Alike 4.0 International"
                            },
                            "description": {"en": ""},
                            "icon": "cc-by-nc-sa-icon",
                            "props": {
                                "url": "https://creativecommons.org/licenses/by-nc-sa/4.0/legalcode",
                                "scheme": "spdx",
                            },
                        }
                    ],
                    "description": "Top 100 books on cultural anthropology.",
                },
                "custom_fields": {
                    "kcr:commons_domain": "hcommons.org",
                    "kcr:submitter_email": "hallqvist.toddgerald.albertson@drexel.edu",
                    "kcr:submitter_username": "albertson",
                    "kcr:user_defined_tags": [
                        "list",
                        "reading",
                        "syllabus",
                        "Cultural anthropology",
                    ],
                    "hclegacy:collection": "hccollection:1",
                    "hclegacy:file_location": "/srv/www/commons/current/web/app/uploads/humcore/o_1bd76kgfsqp91p8nsf1a48osv7.pdf.cultural-anthropology-background-reading.pdf",
                    "hclegacy:file_pid": "hc:11782",
                    "hclegacy:previously_published": "not-published",
                    "hclegacy:record_change_date": "2017-04-08T16:35:59Z",
                    "hclegacy:record_creation_date": "2017-04-08T16:35:59Z",
                    "hclegacy:submitter_org_memberships": ["hc"],
                    "hclegacy:submitter_id": "1008513",
                },
                "access": {
                    "record": "public",
                    "files": "public",
                    "embargo": {"active": false, "reason": null},
                    "status": "open",
                },
                "files": {
                    "enabled": true,
                    "order": [],
                    "count": 1,
                    "total_bytes": 75267,
                    "entries": {
                        "cultural-anthropology-background-reading.pdf": {
                            "ext": "pdf",
                            "key": "cultural-anthropology-background-reading.pdf",
                            "metadata": {},
                            "mimetype": "application/pdf",
                            "size": 75267,
                        }
                    },
                },
                "status": "published",
                "stats": {
                    "this_version": {
                        "views": 0,
                        "unique_views": 0,
                        "downloads": 0,
                        "unique_downloads": 0,
                        "data_volume": 0.0,
                    },
                    "all_versions": {
                        "views": 0,
                        "unique_views": 0,
                        "downloads": 0,
                        "unique_downloads": 0,
                        "data_volume": 0.0,
                    },
                },
            },
            {
                "id": "wyyan-rqg26",
                "created": "2024-02-02T18:33:04.676883+00:00",
                "updated": "2024-02-02T18:33:04.810716+00:00",
                "links": {
                    "self": "https://invenio-dev.hcommons-staging.org/api/records/wyyan-rqg26",
                    "self_html": "https://invenio-dev.hcommons-staging.org/records/wyyan-rqg26",
                    "self_doi": "https://invenio-dev.hcommons-staging.org/doi/10.17613/M6H062",
                    "doi": "https://handle.stage.datacite.org/10.17613/M6H062",
                    "self_iiif_manifest": "https://invenio-dev.hcommons-staging.org/api/iiif/record:wyyan-rqg26/manifest",
                    "self_iiif_sequence": "https://invenio-dev.hcommons-staging.org/api/iiif/record:wyyan-rqg26/sequence/default",
                    "files": "https://invenio-dev.hcommons-staging.org/api/records/wyyan-rqg26/files",
                    "archive": "https://invenio-dev.hcommons-staging.org/api/records/wyyan-rqg26/files-archive",
                    "latest": "https://invenio-dev.hcommons-staging.org/api/records/wyyan-rqg26/versions/latest",
                    "latest_html": "https://invenio-dev.hcommons-staging.org/records/wyyan-rqg26/latest",
                    "draft": "https://invenio-dev.hcommons-staging.org/api/records/wyyan-rqg26/draft",
                    "versions": "https://invenio-dev.hcommons-staging.org/api/records/wyyan-rqg26/versions",
                    "access_links": "https://invenio-dev.hcommons-staging.org/api/records/wyyan-rqg26/access/links",
                    "reserve_doi": "https://invenio-dev.hcommons-staging.org/api/records/wyyan-rqg26/draft/pids/doi",
                    "communities": "https://invenio-dev.hcommons-staging.org/api/records/wyyan-rqg26/communities",
                    "communities-suggestions": "https://invenio-dev.hcommons-staging.org/api/records/wyyan-rqg26/communities-suggestions",
                    "requests": "https://invenio-dev.hcommons-staging.org/api/records/wyyan-rqg26/requests",
                },
                "revision_id": 3,
                "parent": {
                    "id": "pkkyc-7ev98",
                    "communities": {
                        "ids": ["6060e26c-54e3-4f33-8710-1bb89d3672ea"],
                        "default": "6060e26c-54e3-4f33-8710-1bb89d3672ea",
                    },
                },
                "versions": {"is_latest": true, "index": 1},
                "is_published": true,
                "is_draft": false,
                "pids": {
                    "doi": {
                        "identifier": "10.17613/M6H062",
                        "provider": "datacite",
                        "client": "datacite",
                    },
                    "oai": {
                        "identifier": "oai:invenio-dev.hcommons-staging.org:wyyan-rqg26",
                        "provider": "oai",
                    },
                },
                "metadata": {
                    "resource_type": {
                        "id": "presentation-conferencePaper",
                        "title": {"de": "Konferenzbeitrag", "en": "Conference paper"},
                    },
                    "creators": [
                        {
                            "person_or_org": {
                                "type": "personal",
                                "name": "Mitchell, Jonathan Paul",
                                "given_name": "Jonathan Paul",
                                "family_name": "Mitchell",
                                "identifiers": [
                                    {
                                        "identifier": "jpmitchell",
                                        "scheme": "hc_username",
                                    }
                                ],
                            },
                            "role": {"id": "author", "title": {"en": "Author"}},
                        }
                    ],
                    "title": "Expression and The Structure of Behaviour",
                    "publisher": "unknown",
                    "publication_date": "2017",
                    "subjects": [
                        {
                            "id": "http://id.worldcat.org/fast/1765182",
                            "subject": "Continental philosophy",
                            "scheme": "FAST-topical",
                        }
                    ],
                    "languages": [{"id": "eng", "title": {"en": "English"}}],
                    "identifiers": [
                        {"identifier": "hc:11607", "scheme": "hclegacy-pid"},
                        {"identifier": "1000360-2907", "scheme": "hclegacy-record-id"},
                        {"identifier": "10.17613/M6H062", "scheme": "datacite-doi"},
                        {
                            "identifier": "https://doi.org/10.17613/M6H062",
                            "scheme": "url",
                        },
                    ],
                    "rights": [
                        {
                            "id": "arr",
                            "title": {"en": "All Rights Reserved"},
                            "description": {
                                "en": "Proprietary material. No permissions are granted for any kind of copyring or re-use. All rights reserved"
                            },
                            "icon": "copyright",
                            "props": {
                                "url": "https://en.wikipedia.org/wiki/All_rights_reserved"
                            },
                        }
                    ],
                    "description": "This paper is part of a workshop with Donald A. Landes on his book <em>Merleau-Ponty and the Paradoxes of Expression.</em> It summarises the ideas of Merleau-Ponty, and Landes' take on these, before offering some critical comments on Landes' chapter on 'The Structure of Behaviour'.",
                    "additional_descriptions": [
                        {
                            "description": "This paper is part of a workshop with Donald A. Landes on his book Merleau-Ponty and the Paradoxes of Expression. It summarises the ideas of Merleau-Ponty, and Landes' take on these, before offering some critical comments on Landes' chapter on 'The Structure of Behaviour'.",
                            "type": {
                                "id": "other",
                                "title": {"de": "Sonstige", "en": "Other"},
                            },
                        }
                    ],
                },
                "custom_fields": {
                    "meeting:meeting": {
                        "dates": "18 May 2016",
                        "place": "University College Dublin",
                        "title": "Workshop with Donald A. Landes on Merleau-Ponty and the Paradoxes of Expression",
                    },
                    "kcr:commons_domain": "hcommons.org",
                    "kcr:meeting_organization": "University College Dublin",
                    "kcr:submitter_email": "jonathan.mitchell@ucdconnect.ie",
                    "kcr:submitter_username": "jpmitchell",
                    "hclegacy:collection": "hccollection:1",
                    "hclegacy:file_location": "/srv/www/commons/current/web/app/uploads/humcore/2017/05/o_1bhsqic05a811l8s1mbn1bivhk77.pdf.jpmitchell-expression_and_the_structure_of_behaviour.pdf",
                    "hclegacy:file_pid": "hc:11608",
                    "hclegacy:previously_published": "not-published",
                    "hclegacy:record_change_date": "2017-09-10T16:36:31Z",
                    "hclegacy:record_creation_date": "2017-03-23T14:33:16Z",
                    "hclegacy:submitter_org_memberships": ["hc"],
                    "hclegacy:submitter_id": "1008279",
                    "hclegacy:groups_for_deposit": [
                        {"group_name": "Philosophy", "group_identifier": "1000587"}
                    ],
                },
                "access": {
                    "record": "public",
                    "files": "public",
                    "embargo": {"active": false, "reason": null},
                    "status": "open",
                },
                "files": {
                    "enabled": true,
                    "order": [],
                    "count": 1,
                    "total_bytes": 494719,
                    "entries": {
                        "ijpmitchell-expression_and_the_structure_of_behaviour.pdf": {
                            "ext": "pdf",
                            "key": "ijpmitchell-expression_and_the_structure_of_behaviour.pdf",
                            "metadata": {},
                            "mimetype": "application/pdf",
                            "size": 494719,
                        }
                    },
                },
                "status": "published",
                "stats": {
                    "this_version": {
                        "views": 0,
                        "unique_views": 0,
                        "downloads": 0,
                        "unique_downloads": 0,
                        "data_volume": 0.0,
                    },
                    "all_versions": {
                        "views": 0,
                        "unique_views": 0,
                        "downloads": 0,
                        "unique_downloads": 0,
                        "data_volume": 0.0,
                    },
                },
            },
            {
                "id": "mdqtg-pdt62",
                "created": "2024-02-02T18:32:28.452519+00:00",
                "updated": "2024-02-02T18:32:28.577718+00:00",
                "links": {
                    "self": "https://invenio-dev.hcommons-staging.org/api/records/mdqtg-pdt62",
                    "self_html": "https://invenio-dev.hcommons-staging.org/records/mdqtg-pdt62",
                    "self_doi": "https://invenio-dev.hcommons-staging.org/doi/10.17613/M6ZW5P",
                    "doi": "https://handle.stage.datacite.org/10.17613/M6ZW5P",
                    "self_iiif_manifest": "https://invenio-dev.hcommons-staging.org/api/iiif/record:mdqtg-pdt62/manifest",
                    "self_iiif_sequence": "https://invenio-dev.hcommons-staging.org/api/iiif/record:mdqtg-pdt62/sequence/default",
                    "files": "https://invenio-dev.hcommons-staging.org/api/records/mdqtg-pdt62/files",
                    "archive": "https://invenio-dev.hcommons-staging.org/api/records/mdqtg-pdt62/files-archive",
                    "latest": "https://invenio-dev.hcommons-staging.org/api/records/mdqtg-pdt62/versions/latest",
                    "latest_html": "https://invenio-dev.hcommons-staging.org/records/mdqtg-pdt62/latest",
                    "draft": "https://invenio-dev.hcommons-staging.org/api/records/mdqtg-pdt62/draft",
                    "versions": "https://invenio-dev.hcommons-staging.org/api/records/mdqtg-pdt62/versions",
                    "access_links": "https://invenio-dev.hcommons-staging.org/api/records/mdqtg-pdt62/access/links",
                    "reserve_doi": "https://invenio-dev.hcommons-staging.org/api/records/mdqtg-pdt62/draft/pids/doi",
                    "communities": "https://invenio-dev.hcommons-staging.org/api/records/mdqtg-pdt62/communities",
                    "communities-suggestions": "https://invenio-dev.hcommons-staging.org/api/records/mdqtg-pdt62/communities-suggestions",
                    "requests": "https://invenio-dev.hcommons-staging.org/api/records/mdqtg-pdt62/requests",
                },
                "revision_id": 3,
                "parent": {
                    "id": "x1ejr-bdk89",
                    "communities": {
                        "ids": ["6060e26c-54e3-4f33-8710-1bb89d3672ea"],
                        "default": "6060e26c-54e3-4f33-8710-1bb89d3672ea",
                    },
                },
                "versions": {"is_latest": true, "index": 1},
                "is_published": true,
                "is_draft": false,
                "pids": {
                    "doi": {
                        "identifier": "10.17613/M6ZW5P",
                        "provider": "datacite",
                        "client": "datacite",
                    },
                    "oai": {
                        "identifier": "oai:invenio-dev.hcommons-staging.org:mdqtg-pdt62",
                        "provider": "oai",
                    },
                },
                "metadata": {
                    "resource_type": {
                        "id": "presentation-conferencePaper",
                        "title": {"de": "Konferenzbeitrag", "en": "Conference paper"},
                    },
                    "creators": [
                        {
                            "person_or_org": {
                                "type": "personal",
                                "name": "Comer, Todd A.",
                                "given_name": "Todd A.",
                                "family_name": "Comer",
                                "identifiers": [
                                    {"identifier": "comertod", "scheme": "hc_username"}
                                ],
                            },
                            "role": {"id": "author", "title": {"en": "Author"}},
                        }
                    ],
                    "title": "Birth as Ethical Sublime in Joel and Ethan Coen's <em>Fargo</em>",
                    "additional_titles": [
                        {
                            "title": "Birth as Ethical Sublime in Joel and Ethan Coen's Fargo",
                            "type": {
                                "id": "other",
                                "title": {"de": "Sonstiger Titel", "en": "Other"},
                            },
                        }
                    ],
                    "publisher": "unknown",
                    "publication_date": "2017",
                    "subjects": [
                        {
                            "id": "http://id.worldcat.org/fast/924259",
                            "subject": "Film criticism",
                            "scheme": "FAST-topical",
                        }
                    ],
                    "languages": [{"id": "eng", "title": {"en": "English"}}],
                    "identifiers": [
                        {"identifier": "hc:11381", "scheme": "hclegacy-pid"},
                        {"identifier": "1000360-2512", "scheme": "hclegacy-record-id"},
                        {"identifier": "10.17613/M6ZW5P", "scheme": "datacite-doi"},
                        {
                            "identifier": "https://doi.org/10.17613/M6ZW5P",
                            "scheme": "url",
                        },
                    ],
                    "rights": [
                        {
                            "id": "arr",
                            "title": {"en": "All Rights Reserved"},
                            "description": {
                                "en": "Proprietary material. No permissions are granted for any kind of copyring or re-use. All rights reserved"
                            },
                            "icon": "copyright",
                            "props": {
                                "url": "https://en.wikipedia.org/wiki/All_rights_reserved"
                            },
                        }
                    ],
                    "description": "None",
                },
                "custom_fields": {
                    "meeting:meeting": {
                        "dates": "November 4-7, 2010",
                        "place": "Chicago",
                        "title": "MMLA 2010",
                    },
                    "kcr:commons_domain": "hcommons.org",
                    "kcr:meeting_organization": "Midwest Modern Language Association",
                    "kcr:submitter_email": "proftod@gmail.com",
                    "kcr:submitter_username": "comertod",
                    "kcr:user_defined_tags": ["Joel and Ethan Coen", "Sublime"],
                    "hclegacy:collection": "hccollection:1",
                    "hclegacy:file_location": "/srv/www/commons/current/web/app/uploads/humcore/o_1ba2b82ff1cgb1ido5rt41ggp7.pdf.birth_as_ethical_sublime_in_joel_and_et.pdf",
                    "hclegacy:file_pid": "hc:11382",
                    "hclegacy:previously_published": "not-published",
                    "hclegacy:record_change_date": "2017-02-28T14:59:48Z",
                    "hclegacy:record_creation_date": "2017-02-28T12:34:48Z",
                    "hclegacy:submitter_org_memberships": ["hc"],
                    "hclegacy:submitter_id": "1007385",
                    "hclegacy:groups_for_deposit": [
                        {"group_name": "Film Studies", "group_identifier": "1000691"}
                    ],
                },
                "access": {
                    "record": "public",
                    "files": "public",
                    "embargo": {"active": false, "reason": null},
                    "status": "open",
                },
                "files": {
                    "enabled": true,
                    "order": [],
                    "count": 1,
                    "total_bytes": 107164,
                    "entries": {
                        "birth_as_ethical_sublime_in_joel_and_et.pdf": {
                            "ext": "pdf",
                            "key": "birth_as_ethical_sublime_in_joel_and_et.pdf",
                            "metadata": {},
                            "mimetype": "application/pdf",
                            "size": 107164,
                        }
                    },
                },
                "status": "published",
                "stats": {
                    "this_version": {
                        "views": 0,
                        "unique_views": 0,
                        "downloads": 0,
                        "unique_downloads": 0,
                        "data_volume": 0.0,
                    },
                    "all_versions": {
                        "views": 0,
                        "unique_views": 0,
                        "downloads": 0,
                        "unique_downloads": 0,
                        "data_volume": 0.0,
                    },
                },
            },
            {
                "id": "gykv2-9t519",
                "created": "2024-02-02T18:32:16.115624+00:00",
                "updated": "2024-02-02T18:32:16.250010+00:00",
                "links": {
                    "self": "https://invenio-dev.hcommons-staging.org/api/records/gykv2-9t519",
                    "self_html": "https://invenio-dev.hcommons-staging.org/records/gykv2-9t519",
                    "self_doi": "https://invenio-dev.hcommons-staging.org/doi/10.17613/M62048",
                    "doi": "https://handle.stage.datacite.org/10.17613/M62048",
                    "self_iiif_manifest": "https://invenio-dev.hcommons-staging.org/api/iiif/record:gykv2-9t519/manifest",
                    "self_iiif_sequence": "https://invenio-dev.hcommons-staging.org/api/iiif/record:gykv2-9t519/sequence/default",
                    "files": "https://invenio-dev.hcommons-staging.org/api/records/gykv2-9t519/files",
                    "archive": "https://invenio-dev.hcommons-staging.org/api/records/gykv2-9t519/files-archive",
                    "latest": "https://invenio-dev.hcommons-staging.org/api/records/gykv2-9t519/versions/latest",
                    "latest_html": "https://invenio-dev.hcommons-staging.org/records/gykv2-9t519/latest",
                    "draft": "https://invenio-dev.hcommons-staging.org/api/records/gykv2-9t519/draft",
                    "versions": "https://invenio-dev.hcommons-staging.org/api/records/gykv2-9t519/versions",
                    "access_links": "https://invenio-dev.hcommons-staging.org/api/records/gykv2-9t519/access/links",
                    "reserve_doi": "https://invenio-dev.hcommons-staging.org/api/records/gykv2-9t519/draft/pids/doi",
                    "communities": "https://invenio-dev.hcommons-staging.org/api/records/gykv2-9t519/communities",
                    "communities-suggestions": "https://invenio-dev.hcommons-staging.org/api/records/gykv2-9t519/communities-suggestions",
                    "requests": "https://invenio-dev.hcommons-staging.org/api/records/gykv2-9t519/requests",
                },
                "revision_id": 3,
                "parent": {
                    "id": "fnxr1-23p57",
                    "communities": {
                        "ids": ["6060e26c-54e3-4f33-8710-1bb89d3672ea"],
                        "default": "6060e26c-54e3-4f33-8710-1bb89d3672ea",
                    },
                },
                "versions": {"is_latest": true, "index": 1},
                "is_published": true,
                "is_draft": false,
                "pids": {
                    "doi": {
                        "identifier": "10.17613/M62048",
                        "provider": "datacite",
                        "client": "datacite",
                    },
                    "oai": {
                        "identifier": "oai:invenio-dev.hcommons-staging.org:gykv2-9t519",
                        "provider": "oai",
                    },
                },
                "metadata": {
                    "resource_type": {
                        "id": "textDocument-bookSection",
                        "title": {"de": "Buchabteilung", "en": "Book section"},
                    },
                    "creators": [
                        {
                            "person_or_org": {
                                "type": "personal",
                                "name": "Eisenberg, Andrew",
                                "given_name": "Andrew",
                                "family_name": "Eisenberg",
                                "identifiers": [
                                    {
                                        "identifier": "aeisenberg",
                                        "scheme": "hc_username",
                                    }
                                ],
                            },
                            "role": {"id": "author", "title": {"en": "Author"}},
                        }
                    ],
                    "title": "Musical Property Rights Regimes in Tanzania and Kenya after TRIPS",
                    "publisher": "SAGE Publications",
                    "publication_date": "2015",
                    "subjects": [
                        {
                            "id": "http://id.worldcat.org/fast/916186",
                            "subject": "Ethnomusicology",
                            "scheme": "FAST-topical",
                        }
                    ],
                    "contributors": [
                        {
                            "person_or_org": {
                                "type": "personal",
                                "name": "Perullo, Alex",
                                "given_name": "Alex",
                                "family_name": "Perullo",
                            },
                            "role": {
                                "id": "other",
                                "title": {"de": "Andere", "en": "Other"},
                            },
                        },
                        {
                            "person_or_org": {
                                "type": "personal",
                                "name": "Eisenberg, Andrew J.",
                                "given_name": "Andrew J.",
                                "family_name": "Eisenberg",
                            },
                            "role": {
                                "id": "other",
                                "title": {"de": "Andere", "en": "Other"},
                            },
                        },
                    ],
                    "dates": [
                        {
                            "date": "2015-02-13",
                            "type": {
                                "id": "issued",
                                "title": {"de": "Veröffentlicht", "en": "Issued"},
                            },
                            "description": "Publication date",
                        }
                    ],
                    "languages": [{"id": "eng", "title": {"en": "English"}}],
                    "identifiers": [
                        {"identifier": "hc:11311", "scheme": "hclegacy-pid"},
                        {"identifier": "1000360-2373", "scheme": "hclegacy-record-id"},
                        {"identifier": "10.17613/M62048", "scheme": "datacite-doi"},
                        {"identifier": "10.4135/9781473910027.n9", "scheme": "doi"},
                        {
                            "identifier": "https://doi.org/10.17613/M62048",
                            "scheme": "url",
                        },
                    ],
                    "rights": [
                        {
                            "id": "arr",
                            "title": {"en": "All Rights Reserved"},
                            "description": {
                                "en": "Proprietary material. No permissions are granted for any kind of copyring or re-use. All rights reserved"
                            },
                            "icon": "copyright",
                            "props": {
                                "url": "https://en.wikipedia.org/wiki/All_rights_reserved"
                            },
                        }
                    ],
                    "description": "Despite the passage of relatively uniform copyright legislation throughout East Africa and the formation of regional organizations meant to further standardize these laws, the protection of musical works in East African creative industries has varied significantly within and between Tanzania and Kenya. While enforcement remains weak throughout East Africa, each country has also taken a different path in the implementation of copyright policies meant to support musical property rights. These different trajectories can be explained, in large part, by the particular political, social and economic paths taken by East African countries toward the neoliberal present.",
                },
                "custom_fields": {
                    "imprint:imprint": {
                        "title": "The SAGE Handbook of Intellectual Property",
                        "isbn": "9781446266342",
                        "pages": "148-164",
                    },
                    "kcr:commons_domain": "hcommons.org",
                    "kcr:submitter_email": "andrew.eisenberg@nyu.edu",
                    "kcr:submitter_username": "aeisenberg",
                    "kcr:user_defined_tags": [
                        "Copyright",
                        "Intellectual Property",
                        "Kenya",
                        "Tanzania",
                        "African studies",
                    ],
                    "hclegacy:collection": "hccollection:1",
                    "hclegacy:file_location": "/srv/www/commons/current/web/app/uploads/humcore/o_1b9jnn49hesa1kcmmtuj34cd7.pdf.musical-property-rights-regimes-in-tanzania-and-kenya-after-trips.pdf",
                    "hclegacy:file_pid": "hc:11312",
                    "hclegacy:previously_published": "published",
                    "hclegacy:record_change_date": "2017-02-22T20:25:30Z",
                    "hclegacy:record_creation_date": "2017-02-22T20:25:30Z",
                    "hclegacy:submitter_org_memberships": ["hc"],
                    "hclegacy:submitter_id": "1007993",
                },
                "access": {
                    "record": "public",
                    "files": "public",
                    "embargo": {"active": false, "reason": null},
                    "status": "open",
                },
                "files": {
                    "enabled": true,
                    "order": [],
                    "count": 1,
                    "total_bytes": 94057,
                    "entries": {
                        "musical-property-rights-regimes-in-tanzania-and-kenya-after-trips.pdf": {
                            "ext": "pdf",
                            "key": "musical-property-rights-regimes-in-tanzania-and-kenya-after-trips.pdf",
                            "metadata": {},
                            "mimetype": "application/pdf",
                            "size": 94057,
                        }
                    },
                },
                "status": "published",
                "stats": {
                    "this_version": {
                        "views": 0,
                        "unique_views": 0,
                        "downloads": 0,
                        "unique_downloads": 0,
                        "data_volume": 0.0,
                    },
                    "all_versions": {
                        "views": 0,
                        "unique_views": 0,
                        "downloads": 0,
                        "unique_downloads": 0,
                        "data_volume": 0.0,
                    },
                },
            },
            {
                "id": "xy9hc-rmt64",
                "created": "2024-02-02T18:32:10.632217+00:00",
                "updated": "2024-02-02T18:32:10.773709+00:00",
                "links": {
                    "self": "https://invenio-dev.hcommons-staging.org/api/records/xy9hc-rmt64",
                    "self_html": "https://invenio-dev.hcommons-staging.org/records/xy9hc-rmt64",
                    "self_doi": "https://invenio-dev.hcommons-staging.org/doi/10.17613/M6062Z",
                    "doi": "https://handle.stage.datacite.org/10.17613/M6062Z",
                    "self_iiif_manifest": "https://invenio-dev.hcommons-staging.org/api/iiif/record:xy9hc-rmt64/manifest",
                    "self_iiif_sequence": "https://invenio-dev.hcommons-staging.org/api/iiif/record:xy9hc-rmt64/sequence/default",
                    "files": "https://invenio-dev.hcommons-staging.org/api/records/xy9hc-rmt64/files",
                    "archive": "https://invenio-dev.hcommons-staging.org/api/records/xy9hc-rmt64/files-archive",
                    "latest": "https://invenio-dev.hcommons-staging.org/api/records/xy9hc-rmt64/versions/latest",
                    "latest_html": "https://invenio-dev.hcommons-staging.org/records/xy9hc-rmt64/latest",
                    "draft": "https://invenio-dev.hcommons-staging.org/api/records/xy9hc-rmt64/draft",
                    "versions": "https://invenio-dev.hcommons-staging.org/api/records/xy9hc-rmt64/versions",
                    "access_links": "https://invenio-dev.hcommons-staging.org/api/records/xy9hc-rmt64/access/links",
                    "reserve_doi": "https://invenio-dev.hcommons-staging.org/api/records/xy9hc-rmt64/draft/pids/doi",
                    "communities": "https://invenio-dev.hcommons-staging.org/api/records/xy9hc-rmt64/communities",
                    "communities-suggestions": "https://invenio-dev.hcommons-staging.org/api/records/xy9hc-rmt64/communities-suggestions",
                    "requests": "https://invenio-dev.hcommons-staging.org/api/records/xy9hc-rmt64/requests",
                },
                "revision_id": 3,
                "parent": {
                    "id": "na5fx-7g688",
                    "communities": {
                        "ids": ["6060e26c-54e3-4f33-8710-1bb89d3672ea"],
                        "default": "6060e26c-54e3-4f33-8710-1bb89d3672ea",
                    },
                },
                "versions": {"is_latest": true, "index": 1},
                "is_published": true,
                "is_draft": false,
                "pids": {
                    "doi": {
                        "identifier": "10.17613/M6062Z",
                        "provider": "datacite",
                        "client": "datacite",
                    },
                    "oai": {
                        "identifier": "oai:invenio-dev.hcommons-staging.org:xy9hc-rmt64",
                        "provider": "oai",
                    },
                },
                "metadata": {
                    "resource_type": {
                        "id": "textDocument-journalArticle",
                        "title": {
                            "de": "Zeitschriftenartikel",
                            "en": "Journal article",
                        },
                    },
                    "creators": [
                        {
                            "person_or_org": {
                                "type": "personal",
                                "name": "Benassuly, Matheus",
                                "given_name": "Matheus",
                                "family_name": "Benassuly",
                                "identifiers": [
                                    {
                                        "identifier": "mbenassuly",
                                        "scheme": "hc_username",
                                    }
                                ],
                            },
                            "role": {"id": "author", "title": {"en": "Author"}},
                        }
                    ],
                    "title": "Homens de coragem: construção da resistência cotidiana do agricultor Lúcio em torno da construção da barragem de Belo Monte.",
                    "publisher": "unknown",
                    "publication_date": "2017",
                    "subjects": [
                        {
                            "id": "http://id.worldcat.org/fast/810196",
                            "subject": "Anthropology",
                            "scheme": "FAST-topical",
                        },
                        {
                            "id": "http://id.worldcat.org/fast/1749638",
                            "subject": "Environmental sociology",
                            "scheme": "FAST-topical",
                        },
                        {
                            "id": "http://id.worldcat.org/fast/1245945",
                            "subject": "Latin America",
                            "scheme": "FAST-geographic",
                        },
                        {
                            "id": "http://id.worldcat.org/fast/801646",
                            "subject": "Agriculture--Social aspects",
                            "scheme": "FAST-topical",
                        },
                    ],
                    "languages": [{"id": "por", "title": {"en": "Portuguese"}}],
                    "identifiers": [
                        {"identifier": "hc:11279", "scheme": "hclegacy-pid"},
                        {"identifier": "1000360-2310", "scheme": "hclegacy-record-id"},
                        {"identifier": "10.17613/M6062Z", "scheme": "datacite-doi"},
                        {
                            "identifier": "https://doi.org/10.17613/M6062Z",
                            "scheme": "url",
                        },
                    ],
                    "rights": [
                        {
                            "id": "arr",
                            "title": {"en": "All Rights Reserved"},
                            "description": {
                                "en": "Proprietary material. No permissions are granted for any kind of copyring or re-use. All rights reserved"
                            },
                            "icon": "copyright",
                            "props": {
                                "url": "https://en.wikipedia.org/wiki/All_rights_reserved"
                            },
                        }
                    ],
                    "description": "In this work, I analyze the writings of a farmer from Volta Grande do Xingu / PA, Lucio, who begins to write poems, thoughts and reports in the course of the struggle against the construction of the dam that ended up forcing the farmer and his family from their land. In this article, I critique Men of Courage, one of the author's major texts written as he fought the dam. By doing so, I reveal different dimensions of the text, which mobilizes different various categories, agents and stages of political struggle in the resistance against the dam.\n\nO objetivo principal da reflexão proposta por meio deste trabalho é o de exercitar a análise dos escritos de um agricultor de Volta Grande do Xingu/PA, Lúcio, que passa a escrever poemas, pensamentos e relatórios no decorrer da luta contra a barragem que acabou por deslocar compulsoriamente o agricultor e sua família de suas terras. Neste artigo, valorizo um dos principais textos produzido pelo autor ainda no período em que lutava contra a barragem, intitulado Homens de Coragem. A partir da análise foi possível perceber diferentes dimensões do texto, em que são mobilizados variados categorias, agentes e etapas de luta política no curso da resistência contra a barragem.",
                    "additional_descriptions": [
                        {
                            "description": "In this work, I analyze the writings of a farmer from Volta Grande do Xingu / PA, Lucio, who begins to write poems, thoughts and reports in the course of the struggle against the construction of the dam that ended up forcing the farmer and his family from their land. In this article, I critique Men of Courage, one of the author's major texts written as he fought the dam. By doing so, I reveal different dimensions of the text, which mobilizes different various categories, agents and stages of political struggle in the resistance against the dam. O objetivo principal da reflexão proposta por meio deste trabalho é o de exercitar a análise dos escritos de um agricultor de Volta Grande do Xingu/PA, Lúcio, que passa a escrever poemas, pensamentos e relatórios no decorrer da luta contra a barragem que acabou por deslocar compulsoriamente o agricultor e sua família de suas terras. Neste artigo, valorizo um dos principais textos produzido pelo autor ainda no período em que lutava contra a barragem, intitulado Homens de Coragem. A partir da análise foi possível perceber diferentes dimensões do texto, em que são mobilizados variados categorias, agentes e etapas de luta política no curso da resistência contra a barragem.",
                            "type": {
                                "id": "other",
                                "title": {"de": "Sonstige", "en": "Other"},
                            },
                        }
                    ],
                },
                "custom_fields": {
                    "journal:journal": {
                        "title": "Homens de coragem: construção da resistência cotidiana do agricultor Lúcio em torno da construção da barragem de Belo Monte"
                    },
                    "kcr:commons_domain": "hcommons.org",
                    "kcr:submitter_email": "matheusbenassuly@gmail.com",
                    "kcr:submitter_username": "mbenassuly",
                    "kcr:user_defined_tags": [
                        "Belo Monte dam",
                        "Compulsory Displacement",
                        "npm17",
                        "Peasant narratives",
                        "Rural Studies",
                        "Sociology of development",
                    ],
                    "hclegacy:collection": "hccollection:1",
                    "hclegacy:file_location": "/srv/www/commons/current/web/app/uploads/humcore/o_1b9c9ggm51h0111941vbb1fkh1i2v7.pdf.artigo-redes-rurais-final.pdf",
                    "hclegacy:file_pid": "hc:11280",
                    "hclegacy:previously_published": "published",
                    "hclegacy:publication_type": "proceedings-article",
                    "hclegacy:record_change_date": "2017-04-03T15:51:28Z",
                    "hclegacy:record_creation_date": "2017-02-19T22:59:14Z",
                    "hclegacy:submitter_org_memberships": ["hc"],
                    "hclegacy:submitter_id": "1008037",
                },
                "access": {
                    "record": "public",
                    "files": "public",
                    "embargo": {"active": false, "reason": null},
                    "status": "open",
                },
                "files": {
                    "enabled": true,
                    "order": [],
                    "count": 1,
                    "total_bytes": 456734,
                    "entries": {
                        "artigo-redes-rurais-final.pdf": {
                            "ext": "pdf",
                            "key": "artigo-redes-rurais-final.pdf",
                            "metadata": {},
                            "mimetype": "application/pdf",
                            "size": 456734,
                        }
                    },
                },
                "status": "published",
                "stats": {
                    "this_version": {
                        "views": 0,
                        "unique_views": 0,
                        "downloads": 0,
                        "unique_downloads": 0,
                        "data_volume": 0.0,
                    },
                    "all_versions": {
                        "views": 0,
                        "unique_views": 0,
                        "downloads": 0,
                        "unique_downloads": 0,
                        "data_volume": 0.0,
                    },
                },
            },
            {
                "id": "mkw7z-1tv85",
                "created": "2024-02-02T18:31:56.836909+00:00",
                "updated": "2024-02-02T18:31:56.969674+00:00",
                "links": {
                    "self": "https://invenio-dev.hcommons-staging.org/api/records/mkw7z-1tv85",
                    "self_html": "https://invenio-dev.hcommons-staging.org/records/mkw7z-1tv85",
                    "self_doi": "https://invenio-dev.hcommons-staging.org/doi/10.17613/M64927",
                    "doi": "https://handle.stage.datacite.org/10.17613/M64927",
                    "self_iiif_manifest": "https://invenio-dev.hcommons-staging.org/api/iiif/record:mkw7z-1tv85/manifest",
                    "self_iiif_sequence": "https://invenio-dev.hcommons-staging.org/api/iiif/record:mkw7z-1tv85/sequence/default",
                    "files": "https://invenio-dev.hcommons-staging.org/api/records/mkw7z-1tv85/files",
                    "archive": "https://invenio-dev.hcommons-staging.org/api/records/mkw7z-1tv85/files-archive",
                    "latest": "https://invenio-dev.hcommons-staging.org/api/records/mkw7z-1tv85/versions/latest",
                    "latest_html": "https://invenio-dev.hcommons-staging.org/records/mkw7z-1tv85/latest",
                    "draft": "https://invenio-dev.hcommons-staging.org/api/records/mkw7z-1tv85/draft",
                    "versions": "https://invenio-dev.hcommons-staging.org/api/records/mkw7z-1tv85/versions",
                    "access_links": "https://invenio-dev.hcommons-staging.org/api/records/mkw7z-1tv85/access/links",
                    "reserve_doi": "https://invenio-dev.hcommons-staging.org/api/records/mkw7z-1tv85/draft/pids/doi",
                    "communities": "https://invenio-dev.hcommons-staging.org/api/records/mkw7z-1tv85/communities",
                    "communities-suggestions": "https://invenio-dev.hcommons-staging.org/api/records/mkw7z-1tv85/communities-suggestions",
                    "requests": "https://invenio-dev.hcommons-staging.org/api/records/mkw7z-1tv85/requests",
                },
                "revision_id": 3,
                "parent": {
                    "id": "7xynx-h3y59",
                    "communities": {
                        "ids": ["6060e26c-54e3-4f33-8710-1bb89d3672ea"],
                        "default": "6060e26c-54e3-4f33-8710-1bb89d3672ea",
                    },
                },
                "versions": {"is_latest": true, "index": 1},
                "is_published": true,
                "is_draft": false,
                "pids": {
                    "doi": {
                        "identifier": "10.17613/M64927",
                        "provider": "datacite",
                        "client": "datacite",
                    },
                    "oai": {
                        "identifier": "oai:invenio-dev.hcommons-staging.org:mkw7z-1tv85",
                        "provider": "oai",
                    },
                },
                "metadata": {
                    "resource_type": {
                        "id": "textDocument-journalArticle",
                        "title": {
                            "de": "Zeitschriftenartikel",
                            "en": "Journal article",
                        },
                    },
                    "creators": [
                        {
                            "person_or_org": {
                                "type": "personal",
                                "name": "Hartmann, Benjamin",
                                "given_name": "Benjamin",
                                "family_name": "Hartmann",
                                "identifiers": [
                                    {
                                        "identifier": "benhartmann",
                                        "scheme": "hc_username",
                                    }
                                ],
                            },
                            "role": {"id": "author", "title": {"en": "Author"}},
                        }
                    ],
                    "title": "Die hölzernen Schreibtafeln im Imperium Romanum - ein Inventar",
                    "publisher": "RGZM",
                    "publication_date": "2015",
                    "subjects": [
                        {
                            "id": "http://id.worldcat.org/fast/885069",
                            "subject": "Culture--History",
                            "scheme": "FAST-topical",
                        },
                        {
                            "id": "http://id.worldcat.org/fast/973837",
                            "subject": "Inscriptions",
                            "scheme": "FAST-topical",
                        },
                        {
                            "id": "http://id.worldcat.org/fast/1181638",
                            "subject": "Writing",
                            "scheme": "FAST-topical",
                        },
                    ],
                    "languages": [{"id": "deu", "title": {"en": "German"}}],
                    "identifiers": [
                        {"identifier": "hc:11193", "scheme": "hclegacy-pid"},
                        {"identifier": "1000360-2143", "scheme": "hclegacy-record-id"},
                        {"identifier": "10.17613/M64927", "scheme": "datacite-doi"},
                        {"identifier": "10.5281/zenodo.268554", "scheme": "doi"},
                        {
                            "identifier": "https://doi.org/10.17613/M64927",
                            "scheme": "url",
                        },
                    ],
                    "rights": [
                        {
                            "id": "cc-by-nc-sa-4.0",
                            "title": {
                                "en": "Creative Commons Attribution Non Commercial Share Alike 4.0 International"
                            },
                            "description": {"en": ""},
                            "icon": "cc-by-nc-sa-icon",
                            "props": {
                                "url": "https://creativecommons.org/licenses/by-nc-sa/4.0/legalcode",
                                "scheme": "spdx",
                            },
                        }
                    ],
                    "description": "Holztafeln fanden in der römischen Antike weite Verbreitung als Schriftträger. Nichtsdestotrotz sind materielle Überreste von solchen Schreibtafeln bis heute vergleichsweise rar. Dies ist vor allem auf die prekären Überlieferungskonditionen von Holz zurückzuführen. Insbesondere in Mittel- und Westeuropa sowie in Britannien fanden und finden sich bei archäologischen Ausgrabungen in Gebieten mit Feuchtbodenerhaltung dennoch vermehrt hölzerne Schreibtafeln. Das vorliegende kommentierte Inventar der Fundorte von hölzernen Schreibtafeln fasst diese Funde in einer Übersicht zusammen. Aus 63 unterschiedlichen Fundstellen sind zusammen über 2500 Wachstafeln (tabulae ceratae) überliefert. Neun Orte haben zusammen ferner über 1100 der dünneren leaf tablets (tiliae) hervorgebracht. Diese materielle Hinterlassenschaft gibt Einblicke in die vielgestaltigen Ausformungen antiker Schriftlichkeit. Die vielfach auf diesen Schreibtafeln erhaltenen Texte bilden zudem einen unschätzbar wertvollen Fundus zu unterschiedlichsten Aspekten der Geschichte der römischen Antike.",
                },
                "custom_fields": {
                    "journal:journal": {
                        "title": "M. Scholz / M. Horster (Hg.): Lesen und Schreiben in den römischen Provinzen. Schriftliche Kommunikation im Alltagsleben. Akten des 2. Internationalen Kolloquiums von DUCTUS – Association internationale pour l'étude des inscriptions mineures, RGZM Mainz, 15.-17. Juni 2011. RGZM – Tagungen, Band 26. Mainz",
                        "pages": "43-58",
                    },
                    "kcr:commons_domain": "hcommons.org",
                    "kcr:submitter_email": "hartmann.bj@gmail.com",
                    "kcr:submitter_username": "benhartmann",
                    "kcr:user_defined_tags": [
                        "Graffiti",
                        "roman history",
                        "tabula cerata",
                        "Wood",
                        "Ancient history",
                        "Classical studies",
                    ],
                    "hclegacy:collection": "hccollection:1",
                    "hclegacy:file_location": "/srv/www/commons/current/web/app/uploads/humcore/o_1b8ic0pb9p2keja3qg1gfooq7.pdf.hartmann-2015-die-hölzernen-schreibtafeln-im-imperium-romanum-ein-inventar.pdf",
                    "hclegacy:file_pid": "hc:11194",
                    "hclegacy:previously_published": "published",
                    "hclegacy:publication_type": "proceedings-article",
                    "hclegacy:record_change_date": "2017-02-10T13:38:21Z",
                    "hclegacy:record_creation_date": "2017-02-09T21:37:57Z",
                    "hclegacy:submitter_org_memberships": ["hc"],
                    "hclegacy:submitter_id": "1007925",
                    "hclegacy:groups_for_deposit": [
                        {
                            "group_name": "Ancient Greece & Rome",
                            "group_identifier": "1000636",
                        }
                    ],
                },
                "access": {
                    "record": "public",
                    "files": "public",
                    "embargo": {"active": false, "reason": null},
                    "status": "open",
                },
                "files": {
                    "enabled": true,
                    "order": [],
                    "count": 1,
                    "total_bytes": 330432,
                    "entries": {
                        "hartmann-2015-die-hölzernen-schreibtafeln-im-imperium-romanum-ein-inventar.pdf": {
                            "ext": "pdf",
                            "key": "hartmann-2015-die-hölzernen-schreibtafeln-im-imperium-romanum-ein-inventar.pdf",
                            "metadata": {},
                            "mimetype": "application/pdf",
                            "size": 330432,
                        }
                    },
                },
                "status": "published",
                "stats": {
                    "this_version": {
                        "views": 0,
                        "unique_views": 0,
                        "downloads": 0,
                        "unique_downloads": 0,
                        "data_volume": 0.0,
                    },
                    "all_versions": {
                        "views": 0,
                        "unique_views": 0,
                        "downloads": 0,
                        "unique_downloads": 0,
                        "data_volume": 0.0,
                    },
                },
            },
            {
                "id": "3yy8j-03k24",
                "created": "2024-02-02T18:31:22.923398+00:00",
                "updated": "2024-02-02T18:31:23.076067+00:00",
                "links": {
                    "self": "https://invenio-dev.hcommons-staging.org/api/records/3yy8j-03k24",
                    "self_html": "https://invenio-dev.hcommons-staging.org/records/3yy8j-03k24",
                    "self_doi": "https://invenio-dev.hcommons-staging.org/doi/10.17613/M6QG9W",
                    "doi": "https://handle.stage.datacite.org/10.17613/M6QG9W",
                    "self_iiif_manifest": "https://invenio-dev.hcommons-staging.org/api/iiif/record:3yy8j-03k24/manifest",
                    "self_iiif_sequence": "https://invenio-dev.hcommons-staging.org/api/iiif/record:3yy8j-03k24/sequence/default",
                    "files": "https://invenio-dev.hcommons-staging.org/api/records/3yy8j-03k24/files",
                    "archive": "https://invenio-dev.hcommons-staging.org/api/records/3yy8j-03k24/files-archive",
                    "latest": "https://invenio-dev.hcommons-staging.org/api/records/3yy8j-03k24/versions/latest",
                    "latest_html": "https://invenio-dev.hcommons-staging.org/records/3yy8j-03k24/latest",
                    "draft": "https://invenio-dev.hcommons-staging.org/api/records/3yy8j-03k24/draft",
                    "versions": "https://invenio-dev.hcommons-staging.org/api/records/3yy8j-03k24/versions",
                    "access_links": "https://invenio-dev.hcommons-staging.org/api/records/3yy8j-03k24/access/links",
                    "reserve_doi": "https://invenio-dev.hcommons-staging.org/api/records/3yy8j-03k24/draft/pids/doi",
                    "communities": "https://invenio-dev.hcommons-staging.org/api/records/3yy8j-03k24/communities",
                    "communities-suggestions": "https://invenio-dev.hcommons-staging.org/api/records/3yy8j-03k24/communities-suggestions",
                    "requests": "https://invenio-dev.hcommons-staging.org/api/records/3yy8j-03k24/requests",
                },
                "revision_id": 3,
                "parent": {
                    "id": "xwwbq-rw582",
                    "communities": {
                        "ids": ["6060e26c-54e3-4f33-8710-1bb89d3672ea"],
                        "default": "6060e26c-54e3-4f33-8710-1bb89d3672ea",
                    },
                },
                "versions": {"is_latest": true, "index": 1},
                "is_published": true,
                "is_draft": false,
                "pids": {
                    "doi": {
                        "identifier": "10.17613/M6QG9W",
                        "provider": "datacite",
                        "client": "datacite",
                    },
                    "oai": {
                        "identifier": "oai:invenio-dev.hcommons-staging.org:3yy8j-03k24",
                        "provider": "oai",
                    },
                },
                "metadata": {
                    "resource_type": {
                        "id": "textDocument-journalArticle",
                        "title": {
                            "de": "Zeitschriftenartikel",
                            "en": "Journal article",
                        },
                    },
                    "creators": [
                        {
                            "person_or_org": {
                                "type": "personal",
                                "name": "Priego, Ernesto",
                                "given_name": "Ernesto",
                                "family_name": "Priego",
                                "identifiers": [
                                    {
                                        "identifier": "ernestopriego",
                                        "scheme": "hc_username",
                                    }
                                ],
                            },
                            "role": {"id": "author", "title": {"en": "Author"}},
                        }
                    ],
                    "title": "Comics as Research, Comics for Impact: The Case of Higher Fees, Higher Debts",
                    "publisher": "Open Library of Humanities",
                    "publication_date": "2016",
                    "subjects": [
                        {
                            "id": "http://id.worldcat.org/fast/1921613",
                            "subject": "Comics (Graphic works)",
                            "scheme": "FAST-form",
                        },
                        {
                            "id": "http://id.worldcat.org/fast/1726630",
                            "subject": "Graphic novels",
                            "scheme": "FAST-form",
                        },
                        {
                            "id": "http://id.worldcat.org/fast/1095327",
                            "subject": "Research libraries",
                            "scheme": "FAST-topical",
                        },
                    ],
                    "dates": [
                        {
                            "date": "2016-12-28",
                            "type": {
                                "id": "issued",
                                "title": {"de": "Veröffentlicht", "en": "Issued"},
                            },
                            "description": "Publication date",
                        }
                    ],
                    "languages": [{"id": "eng", "title": {"en": "English"}}],
                    "identifiers": [
                        {"identifier": "hc:11027", "scheme": "hclegacy-pid"},
                        {"identifier": "1000360-1914", "scheme": "hclegacy-record-id"},
                        {"identifier": "10.17613/M6QG9W", "scheme": "datacite-doi"},
                        {"identifier": "10.16995/cg.101", "scheme": "doi"},
                        {
                            "identifier": "https://doi.org/10.17613/M6QG9W",
                            "scheme": "url",
                        },
                    ],
                    "rights": [
                        {
                            "id": "cc-by-4.0",
                            "title": {
                                "en": "Creative Commons Attribution 4.0 International"
                            },
                            "description": {
                                "en": "The Creative Commons Attribution license allows re-distribution and re-use of a licensed work on the condition that the creator is appropriately credited."
                            },
                            "icon": "cc-by-icon",
                            "props": {
                                "url": "https://creativecommons.org/licenses/by/4.0/legalcode",
                                "scheme": "spdx",
                            },
                        }
                    ],
                    "description": "Researchers have turned to comics as outputs incorporating their research findings. These comics are print and/or online publications that can lead to the wider adoption of research and enhance educational practices, widen public engagement, and improve the possibilities for research to influence public policy. \n\nThis article presents an interview with Professor Katy Vigurs about Higher Fees, Higher Debts: Greater Expectations of Graduate Futures?, a comic based on a research report produced for the Society for Research into Higher Education (2016). \n\nIn order to contextualize the interview, this article also provides an introduction to non-fiction comics research, and concludes with reflections on comics as a way of doing research. This article seeks to document and encourage further knowledge-exchange between the higher education sector and comics practitioners, and between researchers using comics in their research or as a means to disseminate their own research and those scholars who research comics as their main object of study.",
                    "additional_descriptions": [
                        {
                            "description": "Researchers have turned to comics as outputs incorporating their research findings. These comics are print and/or online publications that can lead to the wider adoption of research and enhance educational practices, widen public engagement, and improve the possibilities for research to influence public policy. This article presents an interview with Professor Katy Vigurs about Higher Fees, Higher Debts: Greater Expectations of Graduate Futures?, a comic based on a research report produced for the Society for Research into Higher Education (2016). In order to contextualize the interview, this article also provides an introduction to non-fiction comics research, and concludes with reflections on comics as a way of doing research. This article seeks to document and encourage further knowledge-exchange between the higher education sector and comics practitioners, and between researchers using comics in their research or as a means to disseminate their own research and those scholars who research comics as their main object of study.",
                            "type": {
                                "id": "other",
                                "title": {"de": "Sonstige", "en": "Other"},
                            },
                        }
                    ],
                },
                "custom_fields": {
                    "journal:journal": {
                        "title": "The Comics Grid: Journal of Comics Scholarship",
                        "issue": "1",
                        "volume": "6",
                        "issn": "2048-0792",
                    },
                    "kcr:commons_domain": "hcommons.org",
                    "kcr:submitter_email": "Ernesto.Priego.1@city.ac.uk",
                    "kcr:submitter_username": "ernestopriego",
                    "kcr:user_defined_tags": [
                        "Higher education",
                        "non-fiction comics",
                        "Research",
                        "scholarly communication",
                        "student finance",
                    ],
                    "hclegacy:collection": "hccollection:1",
                    "hclegacy:file_location": "/srv/www/commons/current/web/app/uploads/humcore/o_1b82ig4ev1iin1ar31ugr1r81soo7.pdf.101-948-1-pb.pdf",
                    "hclegacy:file_pid": "hc:11028",
                    "hclegacy:previously_published": "published",
                    "hclegacy:record_change_date": "2017-02-25T15:15:03Z",
                    "hclegacy:record_creation_date": "2017-02-03T18:07:01Z",
                    "hclegacy:submitter_org_memberships": ["hc"],
                    "hclegacy:submitter_id": "1007798",
                },
                "access": {
                    "record": "public",
                    "files": "public",
                    "embargo": {"active": false, "reason": null},
                    "status": "open",
                },
                "files": {
                    "enabled": true,
                    "order": [],
                    "count": 1,
                    "total_bytes": 1907823,
                    "entries": {
                        "101-948-1-pb.pdf": {
                            "ext": "pdf",
                            "key": "101-948-1-pb.pdf",
                            "metadata": {},
                            "mimetype": "application/pdf",
                            "size": 1907823,
                        }
                    },
                },
                "status": "published",
                "stats": {
                    "this_version": {
                        "views": 0,
                        "unique_views": 0,
                        "downloads": 0,
                        "unique_downloads": 0,
                        "data_volume": 0.0,
                    },
                    "all_versions": {
                        "views": 0,
                        "unique_views": 0,
                        "downloads": 0,
                        "unique_downloads": 0,
                        "data_volume": 0.0,
                    },
                },
            },
            {
                "id": "gwjr3-zz461",
                "created": "2024-02-02T18:31:06.056027+00:00",
                "updated": "2024-02-02T18:31:06.202014+00:00",
                "links": {
                    "self": "https://invenio-dev.hcommons-staging.org/api/records/gwjr3-zz461",
                    "self_html": "https://invenio-dev.hcommons-staging.org/records/gwjr3-zz461",
                    "self_doi": "https://invenio-dev.hcommons-staging.org/doi/10.17613/M6WD1Q",
                    "doi": "https://handle.stage.datacite.org/10.17613/M6WD1Q",
                    "self_iiif_manifest": "https://invenio-dev.hcommons-staging.org/api/iiif/record:gwjr3-zz461/manifest",
                    "self_iiif_sequence": "https://invenio-dev.hcommons-staging.org/api/iiif/record:gwjr3-zz461/sequence/default",
                    "files": "https://invenio-dev.hcommons-staging.org/api/records/gwjr3-zz461/files",
                    "archive": "https://invenio-dev.hcommons-staging.org/api/records/gwjr3-zz461/files-archive",
                    "latest": "https://invenio-dev.hcommons-staging.org/api/records/gwjr3-zz461/versions/latest",
                    "latest_html": "https://invenio-dev.hcommons-staging.org/records/gwjr3-zz461/latest",
                    "draft": "https://invenio-dev.hcommons-staging.org/api/records/gwjr3-zz461/draft",
                    "versions": "https://invenio-dev.hcommons-staging.org/api/records/gwjr3-zz461/versions",
                    "access_links": "https://invenio-dev.hcommons-staging.org/api/records/gwjr3-zz461/access/links",
                    "reserve_doi": "https://invenio-dev.hcommons-staging.org/api/records/gwjr3-zz461/draft/pids/doi",
                    "communities": "https://invenio-dev.hcommons-staging.org/api/records/gwjr3-zz461/communities",
                    "communities-suggestions": "https://invenio-dev.hcommons-staging.org/api/records/gwjr3-zz461/communities-suggestions",
                    "requests": "https://invenio-dev.hcommons-staging.org/api/records/gwjr3-zz461/requests",
                },
                "revision_id": 3,
                "parent": {
                    "id": "n559p-qyv97",
                    "communities": {
                        "ids": ["6060e26c-54e3-4f33-8710-1bb89d3672ea"],
                        "default": "6060e26c-54e3-4f33-8710-1bb89d3672ea",
                    },
                },
                "versions": {"is_latest": true, "index": 1},
                "is_published": true,
                "is_draft": false,
                "pids": {
                    "doi": {
                        "identifier": "10.17613/M6WD1Q",
                        "provider": "datacite",
                        "client": "datacite",
                    },
                    "oai": {
                        "identifier": "oai:invenio-dev.hcommons-staging.org:gwjr3-zz461",
                        "provider": "oai",
                    },
                },
                "metadata": {
                    "resource_type": {
                        "id": "textDocument-journalArticle",
                        "title": {
                            "de": "Zeitschriftenartikel",
                            "en": "Journal article",
                        },
                    },
                    "creators": [
                        {
                            "person_or_org": {
                                "type": "personal",
                                "name": "Steer, Philip",
                                "given_name": "Philip",
                                "family_name": "Steer",
                                "identifiers": [
                                    {"identifier": "pmcsteer", "scheme": "hc_username"}
                                ],
                            },
                            "role": {"id": "author", "title": {"en": "Author"}},
                            "affiliations": [{"name": "Massey U"}],
                        }
                    ],
                    "title": "Gold and Greater Britain: Jevons, Trollope, and Settler Colonialism",
                    "publisher": "Indiana University Press",
                    "publication_date": "2016",
                    "subjects": [
                        {
                            "id": "http://id.worldcat.org/fast/821406",
                            "subject": "Australasian literature",
                            "scheme": "FAST-topical",
                        },
                        {
                            "id": "http://id.worldcat.org/fast/839082",
                            "subject": "British literature",
                            "scheme": "FAST-topical",
                        },
                    ],
                    "dates": [
                        {
                            "date": "2016-10-12",
                            "type": {
                                "id": "issued",
                                "title": {"de": "Veröffentlicht", "en": "Issued"},
                            },
                            "description": "Publication date",
                        }
                    ],
                    "languages": [{"id": "eng", "title": {"en": "English"}}],
                    "identifiers": [
                        {"identifier": "hc:10945", "scheme": "hclegacy-pid"},
                        {"identifier": "1000360-1790", "scheme": "hclegacy-record-id"},
                        {"identifier": "10.17613/M6WD1Q", "scheme": "datacite-doi"},
                        {
                            "identifier": "10.2979/victorianstudies.58.3.02",
                            "scheme": "doi",
                        },
                        {
                            "identifier": "https://doi.org/10.17613/M6WD1Q",
                            "scheme": "url",
                        },
                    ],
                    "rights": [
                        {
                            "id": "arr",
                            "title": {"en": "All Rights Reserved"},
                            "description": {
                                "en": "Proprietary material. No permissions are granted for any kind of copyring or re-use. All rights reserved"
                            },
                            "icon": "copyright",
                            "props": {
                                "url": "https://en.wikipedia.org/wiki/All_rights_reserved"
                            },
                        }
                    ],
                    "description": "The Australian gold rushes of the 1850s provide an exemplary test case for exploring the impact of Greater Britain—the settler colonial empire—on the Victorian novel and political economy. British gold diggers' nomadism operated in seeming antithesis to the colonies' explosive growth, which posed a conceptual challenge both to political economy's stadial model of societal development and to liberal narratives of labor and land—narratives that underpinned concepts of individual character and civil society. Informed by colonial writing and the experience of gold fields, W. S. Jevons's Theory of Political Economy (1871) and Anthony Trollope's John Caldigate (1879) reimagine metropolitan space and subjectivity in settler-colonial terms, helping lay the ground for a deterritorialized, global British identity.",
                },
                "custom_fields": {
                    "journal:journal": {
                        "title": "Victorian Studies",
                        "issue": "3",
                        "volume": "58",
                        "pages": "436-463",
                        "issn": "0042-5222",
                    },
                    "kcr:commons_domain": "hcommons.org",
                    "kcr:submitter_email": "p.steer@massey.ac.nz",
                    "kcr:submitter_username": "pmcsteer",
                    "kcr:user_defined_tags": ["Literature and economics"],
                    "hclegacy:collection": "hccollection:1",
                    "hclegacy:file_location": "/srv/www/commons/current/web/app/uploads/humcore/o_1b7rn8kjjbr7bdr23rvjl19gs7.pdf.gold-and-greater-britain-jevons-trollope-and-settler-colonialism.pdf",
                    "hclegacy:file_pid": "hc:10946",
                    "hclegacy:previously_published": "published",
                    "hclegacy:record_change_date": "2017-09-10T16:43:43Z",
                    "hclegacy:record_creation_date": "2017-02-01T02:15:24Z",
                    "hclegacy:submitter_org_memberships": ["hc", "mla"],
                    "hclegacy:submitter_affiliation": "Massey U",
                    "hclegacy:submitter_id": "1371",
                },
                "access": {
                    "record": "public",
                    "files": "public",
                    "embargo": {"active": false, "reason": null},
                    "status": "open",
                },
                "files": {
                    "enabled": true,
                    "order": [],
                    "count": 1,
                    "total_bytes": 139974,
                    "entries": {
                        "gold-and-greater-britain-jevons-trollope-and-settler-colonialism.pdf": {
                            "ext": "pdf",
                            "key": "gold-and-greater-britain-jevons-trollope-and-settler-colonialism.pdf",
                            "metadata": {},
                            "mimetype": "application/pdf",
                            "size": 139974,
                        }
                    },
                },
                "status": "published",
                "stats": {
                    "this_version": {
                        "views": 0,
                        "unique_views": 0,
                        "downloads": 0,
                        "unique_downloads": 0,
                        "data_volume": 0.0,
                    },
                    "all_versions": {
                        "views": 0,
                        "unique_views": 0,
                        "downloads": 0,
                        "unique_downloads": 0,
                        "data_volume": 0.0,
                    },
                },
            },
        ],
        "total": 15981,
    },
    "aggregations": {
        "access_status": {
            "buckets": [
                {
                    "key": "open",
                    "doc_count": 15881,
                    "label": "Open",
                    "is_selected": false,
                },
                {
                    "key": "metadata-only",
                    "doc_count": 100,
                    "label": "Metadata-only",
                    "is_selected": false,
                },
            ],
            "label": "Access status",
        },
        "file_type": {
            "buckets": [
                {
                    "key": "pdf",
                    "doc_count": 14507,
                    "label": "PDF",
                    "is_selected": false,
                },
                {
                    "key": "docx",
                    "doc_count": 394,
                    "label": "DOCX",
                    "is_selected": false,
                },
                {"key": "mp3", "doc_count": 286, "label": "MP3", "is_selected": false},
                {"key": "mp4", "doc_count": 194, "label": "MP4", "is_selected": false},
                {
                    "key": "pptx",
                    "doc_count": 148,
                    "label": "PPTX",
                    "is_selected": false,
                },
                {"key": "doc", "doc_count": 128, "label": "DOC", "is_selected": false},
                {"key": "jpg", "doc_count": 78, "label": "JPG", "is_selected": false},
                {"key": "html", "doc_count": 34, "label": "HTML", "is_selected": false},
                {"key": "png", "doc_count": 27, "label": "PNG", "is_selected": false},
                {"key": "xlsx", "doc_count": 26, "label": "XLSX", "is_selected": false},
            ],
            "label": "File type",
        },
        "resource_type": {
            "buckets": [
                {
                    "key": "textDocument",
                    "doc_count": 13132,
                    "label": "Text Document",
                    "is_selected": false,
                    "inner": {
                        "buckets": [
                            {
                                "key": "textDocument-journalArticle",
                                "doc_count": 6814,
                                "label": "Journal article",
                                "is_selected": false,
                            },
                            {
                                "key": "textDocument-bookSection",
                                "doc_count": 1660,
                                "label": "Book section",
                                "is_selected": false,
                            },
                            {
                                "key": "textDocument-review",
                                "doc_count": 1567,
                                "label": "Review",
                                "is_selected": false,
                            },
                            {
                                "key": "textDocument-book",
                                "doc_count": 535,
                                "label": "Book",
                                "is_selected": false,
                            },
                            {
                                "key": "textDocument-whitePaper",
                                "doc_count": 458,
                                "label": "White paper",
                                "is_selected": false,
                            },
                            {
                                "key": "textDocument-essay",
                                "doc_count": 401,
                                "label": "Essay",
                                "is_selected": false,
                            },
                            {
                                "key": "textDocument-thesis",
                                "doc_count": 342,
                                "label": "Thesis or dissertation",
                                "is_selected": false,
                            },
                            {
                                "key": "textDocument-abstract",
                                "doc_count": 262,
                                "label": "Abstract",
                                "is_selected": false,
                            },
                            {
                                "key": "textDocument-blogPost",
                                "doc_count": 165,
                                "label": "Blog post",
                                "is_selected": false,
                            },
                            {
                                "key": "textDocument-conferenceProceeding",
                                "doc_count": 152,
                                "label": "Conference proceeding",
                                "is_selected": false,
                            },
                        ]
                    },
                },
                {
                    "key": "presentation",
                    "doc_count": 1123,
                    "label": "Presentation",
                    "is_selected": false,
                    "inner": {
                        "buckets": [
                            {
                                "key": "presentation-conferencePaper",
                                "doc_count": 534,
                                "label": "Conference paper",
                                "is_selected": false,
                            },
                            {
                                "key": "presentation-other",
                                "doc_count": 501,
                                "label": "Other presentation material",
                                "is_selected": false,
                            },
                            {
                                "key": "presentation-conferencePoster",
                                "doc_count": 65,
                                "label": "Conference poster",
                                "is_selected": false,
                            },
                            {
                                "key": "presentation-presentationText",
                                "doc_count": 20,
                                "label": "Presentation text",
                                "is_selected": false,
                            },
                            {
                                "key": "presentation-slides",
                                "doc_count": 2,
                                "label": "Slides",
                                "is_selected": false,
                            },
                        ]
                    },
                },
                {
                    "key": "audiovisual",
                    "doc_count": 645,
                    "label": "Audiovisual",
                    "is_selected": false,
                    "inner": {
                        "buckets": [
                            {
                                "key": "audiovisual-musicalRecording",
                                "doc_count": 514,
                                "label": "Musical recording",
                                "is_selected": false,
                            },
                            {
                                "key": "audiovisual-videoRecording",
                                "doc_count": 87,
                                "label": "Video recording",
                                "is_selected": false,
                            },
                            {
                                "key": "audiovisual-podcastEpisode",
                                "doc_count": 22,
                                "label": "Podcast episode",
                                "is_selected": false,
                            },
                            {
                                "key": "audiovisual-documentary",
                                "doc_count": 9,
                                "label": "Documentary",
                                "is_selected": false,
                            },
                            {
                                "key": "audiovisual-audioRecording",
                                "doc_count": 5,
                                "label": "Audio recording",
                                "is_selected": false,
                            },
                            {
                                "key": "audiovisual-performance",
                                "doc_count": 4,
                                "label": "Performance",
                                "is_selected": false,
                            },
                            {
                                "key": "audiovisual-other",
                                "doc_count": 2,
                                "label": "Other audiovisual material",
                                "is_selected": false,
                            },
                            {
                                "key": "audiovisual-interviewRecording",
                                "doc_count": 1,
                                "label": "Interview recording",
                                "is_selected": false,
                            },
                        ]
                    },
                },
                {
                    "key": "instructionalResource",
                    "doc_count": 459,
                    "label": "Instructional resource",
                    "is_selected": false,
                    "inner": {
                        "buckets": [
                            {
                                "key": "instructionalResource-syllabus",
                                "doc_count": 280,
                                "label": "Syllabus",
                                "is_selected": false,
                            },
                            {
                                "key": "instructionalResource-other",
                                "doc_count": 177,
                                "label": "Other instructional resource",
                                "is_selected": false,
                            },
                            {
                                "key": "instructionalResource-lessonPlan",
                                "doc_count": 1,
                                "label": "Lesson plan",
                                "is_selected": false,
                            },
                        ]
                    },
                },
                {
                    "key": "other",
                    "doc_count": 308,
                    "label": "Other",
                    "is_selected": false,
                    "inner": {
                        "buckets": [
                            {
                                "key": "other-catalog",
                                "doc_count": 25,
                                "label": "Catalog",
                                "is_selected": false,
                            },
                            {
                                "key": "other-patent",
                                "doc_count": 3,
                                "label": "Patent",
                                "is_selected": false,
                            },
                            {
                                "key": "other-workflow",
                                "doc_count": 3,
                                "label": "Workflow",
                                "is_selected": false,
                            },
                            {
                                "key": "other-collection",
                                "doc_count": 1,
                                "label": "Collection",
                                "is_selected": false,
                            },
                            {
                                "key": "other-event",
                                "doc_count": 1,
                                "label": "Event",
                                "is_selected": false,
                            },
                            {
                                "key": "other-notes",
                                "doc_count": 1,
                                "label": "Notes",
                                "is_selected": false,
                            },
                            {
                                "key": "other-peerReview",
                                "doc_count": 1,
                                "label": "Peer review",
                                "is_selected": false,
                            },
                            {
                                "key": "other-physicalObject",
                                "doc_count": 1,
                                "label": "Physical object",
                                "is_selected": false,
                            },
                        ]
                    },
                },
                {
                    "key": "image",
                    "doc_count": 252,
                    "label": "Image",
                    "is_selected": false,
                    "inner": {
                        "buckets": [
                            {
                                "key": "image-other",
                                "doc_count": 175,
                                "label": "Other image",
                                "is_selected": false,
                            },
                            {
                                "key": "image-visualArt",
                                "doc_count": 51,
                                "label": "Visual art",
                                "is_selected": false,
                            },
                            {
                                "key": "image-map",
                                "doc_count": 10,
                                "label": "Map",
                                "is_selected": false,
                            },
                            {
                                "key": "image-chart",
                                "doc_count": 9,
                                "label": "Chart or graph",
                                "is_selected": false,
                            },
                            {
                                "key": "image-figure",
                                "doc_count": 2,
                                "label": "Figure",
                                "is_selected": false,
                            },
                            {
                                "key": "image-photograph",
                                "doc_count": 2,
                                "label": "Photograph",
                                "is_selected": false,
                            },
                        ]
                    },
                },
                {
                    "key": "dataset",
                    "doc_count": 50,
                    "label": "Dataset",
                    "is_selected": false,
                    "inner": {"buckets": []},
                },
                {
                    "key": "software",
                    "doc_count": 12,
                    "label": "Software",
                    "is_selected": false,
                    "inner": {
                        "buckets": [
                            {
                                "key": "software-application",
                                "doc_count": 3,
                                "label": "Application",
                                "is_selected": false,
                            },
                            {
                                "key": "software-computationalNotebook",
                                "doc_count": 3,
                                "label": "Computational notebook",
                                "is_selected": false,
                            },
                            {
                                "key": "software-3DModel",
                                "doc_count": 2,
                                "label": "3D Model",
                                "is_selected": false,
                            },
                            {
                                "key": "software-other",
                                "doc_count": 1,
                                "label": "Other software resource",
                                "is_selected": false,
                            },
                            {
                                "key": "software-service",
                                "doc_count": 1,
                                "label": "Software service",
                                "is_selected": false,
                            },
                        ]
                    },
                },
            ],
            "label": "Resource types",
        },
    },
    "sortBy": "newest",
    "links": {
        "self": "https://invenio-dev.hcommons-staging.org/api/records?page=1&size=25&sort=newest",
        "next": "https://invenio-dev.hcommons-staging.org/api/records?page=2&size=25&sort=newest",
    },
}


def test_total_deposits(requests_mock):
    client = APIclient(token)
    requests_mock.get(
        "https://invenio-dev.hcommons-staging.org/api/records",
        json=return_payload,
    )
    td = client.total_deposits(freq=None, latest=False)
    assert isinstance(td, int)
    print(td)
    assert td < 20000 and td > 10000

