exports.isCharacterMatch = function(string1, string2) {
    return string1.toLowerCase().replace(/[' ']/g, '').split('').sort().join('') === string2.toLowerCase().replace(/[' ']/g, '').split('').sort().join('')
    
};

