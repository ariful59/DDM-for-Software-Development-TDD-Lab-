
class rovar(object):
 
    _LOWER_CONSTANTS = "bcdfhjklmnpqrstvwxz"
    _UPPER_CONSTANTS = "BCFGHJKLMNPQRSTVWXZ"
    VOWEL =  'AEIOU'
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

       
        # builder = ""
        # for c in normal:
        #     if c in self._MODIFIED_LOWER_CONSTANTS:
        #         builder += c+'o'+c
        #     elif c in self._MODIFIED_UPPER_CONSTANTS:
        #         builder += c+'O'+c
        #     else:
        #         builder += c
        builder = []
        for c in normal:
            if c in self._MODIFIED_LOWER_CONSTANTS or c in self._MODIFIED_UPPER_CONSTANTS:
                builder.append(c + 'o' + c)
            else:
                builder.append(c)  # Keep vowels, numbers, and special characters unchanged

        return ''.join(builder)
       
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

        # find = None
        # for c in self._MODIFIED_LOWER_CONSTANTS:
        #     int
        #     if find == (c+'O'+c) or (c+'O'+c):
        #         rov = rov.replace(find, c)
        #
        # for c in self._MODIFIED_UPPER_CONSTANTS:
        #     if find == (c+'O'+c) or (c+'O'+c):
        #         rov = rov.replace(find, c)
        # for double consonant cases
        builder = []
        i = 0
        while i < len(rov):
            c = rov[i]
            # Check for consonant duplication pattern
            if (
                    c in self._MODIFIED_LOWER_CONSTANTS and
                    i + 2 < len(rov) and
                    (rov[i + 1] == 'o' or
                    rov[i + 1] == 'O') and
                    rov[i + 2] == c
            ):
                builder.append(c)
                i += 3
            elif (
                    c in self._MODIFIED_UPPER_CONSTANTS and
                    i + 2 < len(rov) and
                    (rov[i + 1] == 'O' or
                    rov[i + 1] == 'o') and
                    rov[i + 2] == c
            ):
                builder.append(c)
                i += 3  # Skip "COC"
            else:
                builder.append(c)
                i += 1
        return ''.join(builder)
 
        #return rov
