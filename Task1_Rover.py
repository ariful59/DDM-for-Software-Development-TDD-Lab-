import re


class rovar(object):
 
    _LOWER_CONSTANTS = "bcdfhjklmnpqrstvwxz"
    _UPPER_CONSTANTS = "BCFGHJKLMNPQRSTVWXZ"
    VOWEL =  'AEIOUaeiou'
    #ADDED g AND D
    _MODIFIED_LOWER_CONSTANTS = "bcdfghjklmnpqrstvwxz"
    _MODIFIED_UPPER_CONSTANTS = "BCDFGHJKLMNPQRSTVWXZ"
 
    def enrove(self, normal: str)-> str:
        """Encode the string in rovarspraket.
        Args:
            normal (str): Normal string
        Returns:
            (str) Encoded String
        """
        if normal is None:
            return None

        builder = ""
        for c in normal:
            if c in self._MODIFIED_LOWER_CONSTANTS or c in self._MODIFIED_UPPER_CONSTANTS:
                builder += c+'o'+c
            else:
                builder += c
        return builder
 
    def derove(self, rov:str)->str:
        """ 
            Decode a string from rovarspraket.
            Args:
                normal (str): Encoded string
            Returns:
                (str) Normal string
        """
        if rov is None:
            return None

        for c in self._LOWER_CONSTANTS + self._UPPER_CONSTANTS:
            pattern = re.compile(re.escape(c) + r'[oO]' + re.escape(c))  # Matches c + 'o' or 'O' + c
            rov = pattern.sub(c, rov)

        return rov
