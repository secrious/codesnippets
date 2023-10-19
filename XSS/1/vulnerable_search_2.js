// Encoding misses single quote allowing XSS with payload (e.g. '+alert(1)+')
<script>
    <%
        String searchTxt = StringEscapeUtils.escapeHtml4(request.getParameter("search"));
    %>

    document.cookie = 'search=<%=searchTxt%>';
</script>