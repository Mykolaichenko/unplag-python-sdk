"""
This module represents check abstraction in Unplag.
"""


class Check(object):
    """ Representation of Check abstact in Unplag """

    def __init__(self, oauth_session, server):
        self.oauth_session = oauth_session
        self.server = server

    def create(self, file_id, type='web', exclude_citations=0, exclude_references=0):
        """
        Start check for file id

        :param file_id: int
        :param type: respesents type of check, alowed is
                    "my_library", "web", "external_database", "doc_vs_docs", "web_and_my_library"
        :param exclude_citations: boolean
        :param exclude_references: boolean
        :return: request responce, string
        """

        parameters = {
            "type": type,
            "file_id": file_id,
            "exclude_citations": exclude_citations,
            "exclude_references": exclude_references
        }

        resp = self.oauth_session.post(self.server + '/api/v2/check/create', data=parameters)
        return resp.text

    def delete(self, id):
        """
        Delete check for check id

        :param id: check id (string or int)
        :return: responce string
        """
        resp = self.oauth_session.post(self.server + '/api/v2/check/delete', data={"id": id})
        return resp.text

    def generate_pdf(self, id, lang="en_EN"):
        """
        Generate pdf for check id

        :param id: finished check id
        :param lang: main report language "en_EN", "uk_UA", "es_ES", "nl_BE"
        :return:responce string
        """

        resp = self.oauth_session.post(self.server + '/api/v2/check/generate_pdf', data={"id": id, "lang": lang})
        return resp.text

    def get(self, id):
        """
        Get info about check

        :param id: check id
        :return: responce string
        """
        resp = self.oauth_session.get(self.server + '/api/v2/check/get?id=%s' % id)
        return resp.text

    def get_report_link(self, id, lang='en_EN', show_lang_picker=0):
        # TODO: check this one more time
        resp = self.oauth_session.get(self.server + '/api/v2/check/get_report_link?id=%s?lang=%s?show_lang_picker=%s' % (id, lang, show_lang_picker))
        return resp.text

    def toogle_citations(self, id, exclude_citations, exclude_references):
        """
        Exclude citations or references for check

        :param id: check id
        :param exclude_citations: bool
        :param exclude_references: bool
        :return: responce string
        """

        parameters = {
            "id": id,
            "exclude_citations": exclude_citations,
            "exclude_references": exclude_references
        }

        resp = self.oauth_session.post(self.server + '/api/v2/check/toggle', data=parameters)
        return resp.text

    def track_progress(self, id):
        """
        Track progress for check

        :param id: check id
        :return: responce string
        """

        resp = self.oauth_session.get(self.server + '/api/v2/check/progress?id=%s' % id)
        return resp.text