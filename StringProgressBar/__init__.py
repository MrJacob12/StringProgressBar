class progressBar():
    def createBox(value, maxValue, size):
        percentage = value / maxValue
        progress = round((size * percentage))
        emptyProgress = size - progress
        
        progressText = '▇'
        emptyProgressText = '—'
        percentageText = str(round(percentage * 100)) + '%'
        
        bar = '[' + progressText*progress + emptyProgressText*emptyProgress + ']' + percentageText
        return bar

    def createBoxDiscord(value, maxValue, size):
        percentage = value / maxValue
        progress = round((size * percentage))
        emptyProgress = size - progress
        
        progressText = '▇'
        emptyProgressText = '—'
        percentageText = str(round(percentage * 100)) + '%'
        
        bar = '```[' + progressText*progress + emptyProgressText*emptyProgress + ']' + percentageText + '```'
        return bar